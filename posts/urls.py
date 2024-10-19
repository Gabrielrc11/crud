from django.urls import path
from .views import PostListCreateView, PostDetailView,AllPostsListView,PostDeleteView,PostUpdateView

urlpatterns = [
    path('tasks/', PostListCreateView.as_view(), name='post-list-create'),
    path('tasks/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('tasks/all/', AllPostsListView.as_view(), name='all-post-list'),  
    path('tasks/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'), 
    path('tasks/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'), 
]