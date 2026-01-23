from django.contrib import admin
from django.urls import path
from .views import home # This must exist!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # This is what removes the rocket
]