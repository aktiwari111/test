from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
 
)
from . import views

urlpatterns = [
    path('main', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   
    path('about/', views.about, name='blog-about'),
    path('technical_courses', views.technicalcourses, name='technical-courses'),
    path('',views.front,name = 'front-page'),
]
