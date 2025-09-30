from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('posts/<int:post_id>', views.post, name='post'),
    path('posts/new', views.post_new, name='post_new'),
]
