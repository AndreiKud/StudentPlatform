from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='platform-home'),
    path('about/', views.about, name='platform-about'),
]