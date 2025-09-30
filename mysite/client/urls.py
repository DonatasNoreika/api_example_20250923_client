from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('posts/<int:post_id>', views.post, name='post'),
    path('posts/new', views.post_new, name='post_new'),
    path('posts/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete', views.post_delete, name='post_delete'),
]
