
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('base.urls')),
    path('', views.home, name='home'),
    path('diseaseprediction', views.disease, name='diseaseprediction'),
]
