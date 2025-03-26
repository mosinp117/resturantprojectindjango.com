
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resturant/', include('Base_App.urls')),
    path('', HomeView,name="Home"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)