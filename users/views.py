from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
)  # required to be logged in to see profile page
from .forms import UserRegisterForm  # import the login form for users on forms.py
from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm
from main import models
from django.core.paginator import Paginator  # email
from django.core.mail import send_mail  # email
from django.conf import settings  # email
from django.template.loader import render_to_string


# views render logic for the routes


def register(request):  # command to register the user to the database
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save credentials if valid
            username = form.cleaned_data.get("username")  # get username
            messages.success(
                request,
                f"Welcome {username} your account has just been created ! Please log in back to select the institution you study at :)",
            )  # alert menssage
            user_email = form.cleaned_data.get(
                "email"
            )  # get user email, and send email confirming post if valid
            template = render_to_string("users/email_template.html", {"name": username})
            send_mail(
                f"Welcome to BookED {username} !!!",
                template,
                "booked.reset@gmail.com",
                [user_email],
                fail_silently=False,
            )
            return redirect("login")  # redirect to main page
    else:
        form = UserRegisterForm()
    return render(
        request, "users/register.html", {"form": form}
    )  # keeps on the screen what the user wrote if it reloads because of invalid credentials


@login_required  # adds functionality to the function
def profile(request):  # command to login user

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f" Your account has been updated!"
            )  # alert menssage
            return redirect("profile")  # redirect to profile
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "users/profile.html", context)  # display profile


def load_course(request):
    school_id = request.GET.get("school_id")
    courses = models.Course.objects.filter(school_id=school_id)
    return render(
        request, "users/course_dropdown_list_options.html", {"courses": courses}
    )
