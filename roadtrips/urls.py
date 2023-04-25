from . import views
from django.urls import path


urlpatterns = [
    path('roadtrips/', views.PostList.as_view(), name='roadtrips'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
