from django.urls import path
from manager.views import index


urlpatterns = [
    path('', index),
]