from django.urls import path
from . import views
from jobs import views as job_views

urlpatterns = [
    path('', views.home, name='warranty_home'),
    path('About/', views.about, name='warranty_about'),
    path('appointment/', job_views.appointment, name='appointment'),
]