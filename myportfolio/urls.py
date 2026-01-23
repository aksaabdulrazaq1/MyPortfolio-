from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django_distill import distill_path # Import this!
from .views import home

# This function tells distill what to name the file (index.html)
def get_index():
    return None

urlpatterns = [
    path('admin/', admin.site.urls),
    # Change 'path' to 'distill_path' for the homepage
    distill_path('', home, name='home', distill_func=get_index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)