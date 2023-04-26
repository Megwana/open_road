from . import views
from django.urls import path


urlpatterns = [
    path('roadtrips/', views.PostList.as_view(), name='roadtrips'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', views.DeleteUpdate.as_view(), name='post_delete'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
