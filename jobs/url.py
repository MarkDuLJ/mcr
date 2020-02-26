from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='warranty_home'),
    path('About/', views.about, name='warranty_about'),
]