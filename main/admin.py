from django.contrib import admin
from .models import Post, Semester, School, Course, Class, Report_User


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("date_posted",)


class UserRepAdmin(admin.ModelAdmin):
    list_display = ("short_explanation", "author")
    list_filter = ("date_posted",)


admin.site.register(Post, PostAdmin)
admin.site.register(School)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Report_User, UserRepAdmin)
