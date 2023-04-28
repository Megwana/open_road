from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('summernote/', include('django_summernote.urls')),
    path('', include('website.urls'), name='website_urls'),
    path('roadtrips/', include('roadtrips.urls'), name='roadtrips_urls'),
    path('accounts/', include('allauth.urls')),
]
