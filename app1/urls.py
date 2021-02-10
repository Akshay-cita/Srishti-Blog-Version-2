from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
    path('home/', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
    path('register/', views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='app1/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='app1/logout.html'),name='logout'), 
    path('profile/', views.profile,name='profile'),
    
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)