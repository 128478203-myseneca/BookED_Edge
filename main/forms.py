from django import forms
from .models import Post, Course
from captcha.fields import CaptchaField


class PostCreateForm(forms.ModelForm):  # sets up form to create new post /post/new
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "schools",
            "semester",
            "isbn",
            "post_img",
            "course",
            "classes",
            "visible",
        ]
