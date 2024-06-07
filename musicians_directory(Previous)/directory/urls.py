# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.musician_list, name='musician_list'),
#     path('musician/create/', views.musician_create, name='musician_create'),
#     path('musician/<int:pk>/edit/', views.musician_update, name='musician_update'),
#     path('musician/<int:pk>/delete/', views.musician_delete, name='musician_delete'),
#     path('album/create/', views.album_create, name='album_create'),
#     path('album/<int:pk>/edit/', views.album_update, name='album_update'),
#     path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicianListView.as_view(), name='musician_list'),
    path('musician/create/', views.MusicianCreateView.as_view(), name='musician_create'),
    path('musician/<int:pk>/update/', views.MusicianUpdateView.as_view(), name='musician_update'),
    path('musician/<int:pk>/delete/', views.MusicianDeleteView.as_view(), name='musician_delete'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
]