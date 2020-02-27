from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'job/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'job/about.html', {'title': 'About'})
