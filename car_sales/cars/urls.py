from django.urls import path
from .views import HomeView, CarDetailView, BuyCarView, OrderHistoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('buy/<int:pk>/', BuyCarView.as_view(), name='buy-car'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
]
