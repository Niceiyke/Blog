from django.urls import path
from .views import ListCreatePost,SinglePost


urlpatterns = [
 path('',ListCreatePost.as_view(),name='list_create_post'),
 path('post/<pk>',SinglePost.as_view(),name='single_post'),

 
]
