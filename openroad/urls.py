from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'), name='website_urls'),
    path('roadtrips/', include('roadtrips.urls'), name='roadtrips_urls'),
    path('accounts/', include('allauth.urls')),
    path('test_404/', TemplateView.as_view(template_name='404.html')),
    path('test_500/', TemplateView.as_view(template_name='500.html')),
]
