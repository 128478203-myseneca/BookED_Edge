from django.contrib import admin
from .models import Post, Semester, School, Course, Class

admin.site.register(Post)
admin.site.register(School)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Class)
