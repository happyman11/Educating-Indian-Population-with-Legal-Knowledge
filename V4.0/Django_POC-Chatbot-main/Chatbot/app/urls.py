from django.urls import path

from .views import Get_Configuration

urlpatterns = [
    path("extension/config",Get_Configuration.as_view(), name="configuration_it"),
    
]