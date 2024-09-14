from django.urls import path 
from .views import HomePageView
# 'path' es 'ruta'

urlpatterns = [

    path("post/", HomePageView.as_view())      # En las URLS escribir slash '/' luego del nombre 
]