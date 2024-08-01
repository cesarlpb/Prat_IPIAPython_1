
from django.contrib import admin
from django.urls import path
from proyecto_7_app.views import search_pattern, home
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("algoritmoKMP/",search_pattern, name = "algoritmo KMP"),
    path("",home),
    ]   


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    