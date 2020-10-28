from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.paginator import Paginator


class School(models.Model):
    name = models.CharField(max_length=200, default='not declared', null=True, blank=True)


    class Meta:
        verbose_name_plural = "Schools"
        ordering = ["name"]


    def __str__(self):                           
        return self.name

class Semester(models.Model):
    semester = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "Semesters"
       


    def __str__(self):
        return self.semester

class Course(models.Model):
    name = models.CharField(max_length=200, default='not declared')
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True, blank=True)
 
    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["name"]


    def __str__(self):
        return self.name



class Class(models.Model):
    name = models.CharField(max_length=200, default='not declared' )
   # course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
   # semester = models.ManyToManyField(Semester)
    
    class Meta:
        verbose_name_plural = "Classes"
        ordering = ["name"]


    def __str__(self):
        return self.name        


class Post(models.Model):
    title = models.CharField(max_length=50) #title length restriction 50
    content = models.TextField(max_length=500) #content lenght restricted to 500
    schools = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    classes = models.ManyToManyField(Class)
    date_posted = models.DateTimeField(default=timezone.now) #gets time that the post is made
    semester = models.ForeignKey('Semester', null=True, blank=True, on_delete=models.CASCADE)
    objects = models.Manager()
    isbn = models.IntegerField(default=000)
    post_img = models.ImageField(upload_to='post_image',default='default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE) #deleted post if user is deleted
    sponsored = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title

    def save(self, **kwargs):
            super().save()

            img = Image.open(self.post_img.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.post_img.path)

    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk}) #when person creates post redirects itself to the created post after submitted

    class Meta:
        ordering = ['-date_posted']

