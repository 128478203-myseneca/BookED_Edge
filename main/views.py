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
    return render(request,"main/filter2.html", context)



def filters(request):
    schools_all = School.objects.all()
    qs = Post.objects.all()
    title_contains_query = request.GET.get('title_contains')
    isbn_query = request.GET.get('title_or_author')
    semester_query = request.GET.get('semester')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    schools_query = request.GET.get('schools')
    sponsored_query = request.GET.get('sponsored')
    
    if is_calid_queryparam(title_contains_query): #only display books that matches the query
        qs = qs.filter(title__icontains=title_contains_query) 

    if is_calid_queryparam(isbn_query): #only display books that matches the query
        qs = qs.filter(isbn__icontains=isbn_query) 

    if is_calid_queryparam(semester_query):
        qs = qs.filter(semester=semester_query) 

    if is_calid_queryparam(date_min):
        qs = qs.filter(date_posted__gte=date_min)
        
    if is_calid_queryparam(date_max):
        qs = qs.filter(date_posted__lt=date_max)

    if is_calid_queryparam(schools_query) and schools_query != 'Institution You are Engaged':
        qs = qs.filter(schools__name=schools_query)

    if sponsored_query == 'on':
        qs = qs.filter(sponsored=True)

    context = {
        'queryset' : qs,
        'schools_all' : schools_all
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
    fields=['title','content','schools','semester','isbn'] 

    def form_valid(self, form):
        form.instance.author = self.request.user #get users name to put on the post
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #sets up form to update new post /post/new
    model = Post
    fields=['title','content','schools','semester','isbn'] 

    def form_valid(self, form):
        form.instance.author = self.request.user #get users name to put on the post
        return super().form_valid(form)

    def test_func(self): #blocks user from editing posts that are not theirs
        post = self.get_object()
        if self.request.user == post.author:
            return True  
        return False