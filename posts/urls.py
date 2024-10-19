from django.urls import path
from .views import PostListCreateView, PostDetailView,AllPostsListView,PostDeleteView,PostUpdateView

urlpatterns = [
    path('movies/', PostListCreateView.as_view(), name='post-list-create'),
    path('movies/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('movies/all/', AllPostsListView.as_view(), name='all-post-list'),  
    path('movies/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'), 
    path('movies/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'), 
]