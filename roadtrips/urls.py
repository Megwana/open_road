from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='roadtrips'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
