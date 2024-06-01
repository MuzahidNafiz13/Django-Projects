from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('author/', include('Author.urls')), 
    path('profiles/', include('Profiles.urls')), 
    path('post/', include('Posts.urls')), 
    path('category/', include('Categories.urls')), 
]
