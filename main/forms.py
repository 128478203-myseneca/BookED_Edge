from django import forms
from .models import Post, Course

class PostCreateForm(forms.ModelForm): #sets up form to create new post /post/new

    class Meta:
        model = Post
        fields=['title','content','schools','semester','isbn','post_img','course','classes','visible'] 
