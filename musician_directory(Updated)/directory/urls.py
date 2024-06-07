from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.MusicianListView.as_view(), name='musician_list'),
    path('musician/create/', views.MusicianCreateView.as_view(), name='musician_create'),
    path('musician/<int:pk>/update/', views.MusicianUpdateView.as_view(), name='musician_update'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='directory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/', http_method_names=['get', 'post']), name='logout'),    # path('register/', auth_views.RegisterView.as_view(), name='register'),

]