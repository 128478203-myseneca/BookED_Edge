from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from newsapi import NewsApiClient
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #forces user to login before it has access to certain pages, or edit posts
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView )
from .models import Post, School, Semester, Course, Book
from .models import Class as Classes
import datetime as dt
from django.core.paginator import Paginator
import users
from django.shortcuts import redirect
from django.contrib import messages
from .filters import PostFilter


#News API
newsapi = NewsApiClient('c368efff5ae140c896773ec0e2dcae10')
data = newsapi.get_everything(q='education canada', language='en',page_size=20, sort_by='relevancy',domains='theglobeandmail.com')

#logic for news page
def home(request):
    context = {
        'articles' : data['articles']
    } 
    return render(request, 'main/home.html', context)

def is_calid_queryparam(param):
    return param != '' and param is not None

#testing second filter
def filters2(request):
    qs = Book.objects.all()
    schools_all = School.objects.all()
    course_all = Course.objects.all()
    classes_all = Classes.objects.all()
    schools_query = request.GET.get('schools')
    semester_query = request.GET.get('semester')
    classes_query = request.GET.get('classes')
    course_query = request.GET.get('course')

    if is_calid_queryparam(classes_query) and classes_query != 'Class You are Engaged': #only display books that matches the query
        qs = qs.filter(classes__name=classes_query) 

    if is_calid_queryparam(course_query) and course_query != 'Course You are Engaged':
        qs = qs.filter(course__name=course_query) 

    if is_calid_queryparam(schools_query) and schools_query != 'Institution You are Engaged':
        qs = qs.filter(schools__name=schools_query)

    if is_calid_queryparam(semester_query):
        qs = qs.filter(semester=semester_query) 

    context = {
        'queryset2' : qs,
        'schools_all' : schools_all,
        'course_all' : course_all,
        'classes_all' : classes_all,
    }
    return render(request,"main/filter2.html", context) # end filter2

#start of filter/find your book
def filters(request):

    if  request.user.is_anonymous: #return to main page if it is anonymous

        messages.warning(request, f'Please create a account to use the filter feature !!!') #alert menssage
        return redirect('login')
       

    else:

        schools_all = request.user.profile.school
        course_all = request.user.profile.course
        classes_all = request.user.profile.classes
        semester_all = request.user.profile.semester
        #schools_all = School.objects.order_by('name') #alphabetical order
        #course_all = Course.objects.order_by('name') #alphabetical order
        #classes_all = Classes.objects.order_by('name') #alphabetical order
        qs = Post.objects.all() #Post.objects.all().order_by('-date_posted')
        title_contains_query = request.GET.get('title_contains')
        isbn_query = request.GET.get('title_or_author')
        semester_query = request.GET.get('semester')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')
        schools_query = request.GET.get('schools')
        sponsored_query = request.GET.get('sponsored')
        classes_query = request.GET.get('classes')
        course_query = request.GET.get('course')

        #only display books that matches the queries

        if is_calid_queryparam(title_contains_query): 
            qs = qs.filter(title__icontains=title_contains_query) 

        if is_calid_queryparam(isbn_query): 
            qs = qs.filter(isbn__icontains=isbn_query) 

        if is_calid_queryparam(semester_query):
            qs = qs.filter(semester=semester_query) 

        if is_calid_queryparam(date_min):
            qs = qs.filter(date_posted__gte=date_min)
            
        if is_calid_queryparam(date_max):
            qs = qs.filter(date_posted__lt=date_max)

        if is_calid_queryparam(schools_query) and schools_query != 'Institution You are Engaged':
            qs = qs.filter(schools__name=schools_query)

        if is_calid_queryparam(classes_query) and classes_query != 'Class You are Engaged': 
            qs = qs.filter(classes__name=classes_query) 

        if is_calid_queryparam(course_query) and course_query != 'Course You are Engaged':
            qs = qs.filter(course__name=course_query) 

        if sponsored_query == 'on':
            qs = qs.filter(sponsored=True)


        filtered_post = PostFilter( request.GET, queryset=qs)

        paginated_filtered_posts = Paginator(filtered_post.qs, 5)
        page_number = request.GET.get('page')
        post_page_obj = paginated_filtered_posts.get_page(page_number)
        #gotta put here everthing that goes to the html page
        context = {
            'queryset' : qs,
            'schools_all' : schools_all,
            'course_all' : course_all,
            'classes_all' : classes_all,
            'semester_all': semester_all,
            'post_page_obj' : post_page_obj
        }
        return render(request,"main/filters.html", context)

#logic for marketplace view and ordering of posts
class PostListView(ListView):
    model = Post
    template_name = 'main/market.html' # <app>/<models>_<viewtype>.html <APP>
    context_object_name = 'posts' #<MODELS>
    ordering =  ['-date_posted']
    paginate_by = 3


#makes pagination of user_posts
class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_posts.html' # <app>/<models>_<viewtype>.html <APP>
    context_object_name = 'posts' #<MODELS>
    ordering =  ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView): #show /post/<number> pages
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post
    success_url = '/'

    def test_func(self): #blocks user from editing posts that are not theirs
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

        

class PostCreateView(LoginRequiredMixin, CreateView): #sets up form to create new post /post/new
    model = Post
    fields=['title','content','schools','semester','isbn','post_img','course','classes'] 

    def form_valid(self, form):
        form.instance.author = self.request.user #get users name to put on the post
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #sets up form to update new post /post/new
    model = Post
    fields=['title','content','schools','semester','isbn','post_img','course','classes'] 

    def form_valid(self, form):
        form.instance.author = self.request.user #get users name to put on the post
        return super().form_valid(form)

    def test_func(self): #blocks user from editing posts that are not theirs
        post = self.get_object()
        if self.request.user == post.author:
            return True  
        return False