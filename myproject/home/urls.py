from django.urls import path
from . import views

urlpatterns = [
    path('API/', views.API, name='home-API'),
]