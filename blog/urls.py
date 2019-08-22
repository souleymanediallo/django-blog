from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/<slug:category_slug>/', views.post_list, name="post_list_by_category"),
    path('posts/d/<slug:post_slug>/', views.post_detail, name="post_detail"),
]