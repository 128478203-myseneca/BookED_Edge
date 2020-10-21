from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import main
from django.contrib.auth.forms import UserCreationForm



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one relationship with the user profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #default profile image
    image_back = models.ImageField(default='default_back.jpg', upload_to='background_pics') #default profile image
    school = models.ForeignKey(main.models.School, blank= True, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(main.models.Course, blank= True, on_delete=models.CASCADE, null=True)
    classes = models.ForeignKey(main.models.Class, blank= True, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(main.models.Semester, blank= True, on_delete=models.CASCADE, null=True)
    

    def __str__(self): #if you dont have it the page onlsschools will display "profile object" tunder
        return f'{self.user.username} Profile'
       
    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




#note do not forget to make the migrations:
'''
python3 manage.py makemigrations
python3 manage.py migrate
then go to admin.py and add this : from .models import Profile
'''