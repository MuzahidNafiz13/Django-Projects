from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cars.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('cars/', include('cars.urls')),
] 
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)