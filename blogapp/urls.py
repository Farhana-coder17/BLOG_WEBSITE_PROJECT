from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Show all posts
    path('create/', views.create_post, name='create_post'),  # Create Post
    path('update/<int:post_id>/', views.update_post, name='update_post'),  # Update Post
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete Post
]
