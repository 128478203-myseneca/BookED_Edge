from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import main
from captcha.fields import CaptchaField


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["school", "course", "classes", "semester", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["course"].queryset = main.models.Course.objects.none()

        if "school" in self.data:
            school_id = int(self.data.get("school"))
            self.fields["course"].queryset = main.models.Course.objects.filter(
                school_id=school_id
            ).all()

        elif self.instance.pk:
            try:
                self.fields["course"].queryset = self.instance.school.course_set.all()
            except:
                pass


class UserRegisterForm(UserCreationForm):

    # OPTIONS = (main.models.School)
    email = (
        forms.EmailField()
    )  # set required=False if you don't want to force the user to input it
    captcha = CaptchaField()

    class Meta:  # gives netet name space for configuration in one place so whenever you save it gonna save to the user model
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]  # fields in the form and in what order


class UserUpdateForm(forms.ModelForm):

    email = (
        forms.EmailField()
    )  # set required=False if you don't want to force the user to input it

    class Meta:  # gives netet name space for configuration in one place so whenever you save it gonna save to the user model
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]  # fields in the form and in what order
