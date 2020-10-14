from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import main


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['school','course','classes','semester','image']


class UserRegisterForm(UserCreationForm):

    #OPTIONS = (main.models.School)
    email = forms.EmailField() #set required=False if you don't want to force the user to input it
    #school = forms.ChoiceField(choices=OPTIONS,label="", initial='', widget=forms.Select(), required=True)
    
    
    class Meta: #gives netet name space for configuration in one place so whenever you save it gonna save to the user model
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2'] #fields in the form and in what order

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField() #set required=False if you don't want to force the user to input it
    
    

    class Meta: #gives netet name space for configuration in one place so whenever you save it gonna save to the user model
        model = User
        fields = ['first_name','last_name', 'email'] #fields in the form and in what order

