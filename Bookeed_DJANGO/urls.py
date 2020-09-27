from django.conf import settings #alllow profile picture display
from django.conf.urls.static import static  #alllow profile picture display
from django.contrib import admin
from django.contrib.auth import views as auth_views  #login/logout forms
from django.urls import path, include
from users import views as user_views #register forms



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #redirects to users/login
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #redirects to users/logout
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('main.urls')),
     path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   