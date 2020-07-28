from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	
    path('home/', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('register/', views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='app1/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='app1/logout.html'),name='logout'), 
     path('profile/', views.profile,name='profile'),
    
]
