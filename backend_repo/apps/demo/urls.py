from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/<uuid:post_id>/', views.PostView.as_view()),
    path('posts/<uuid:post_id>/comments/', views.CommentListView.as_view()),
    path('posts/<uuid:post_id>/comments/<uuid:comment_id>/', views.CommentView.as_view()),
    
    # random comments
    path('posts/<uuid:post_id>/random-comments/', views.RandomCommentListView.as_view()),
] 
