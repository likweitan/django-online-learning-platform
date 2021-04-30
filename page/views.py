from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path

from django.contrib.auth.decorators import login_required
from .models import Update
from django.contrib.auth.models import User, Group


@login_required
def home_view(request, *args, **kwargs):  # *args, **kwargs
    update_list = Update.objects.all()
    context = {'update_list': update_list}
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", context)


@login_required
def update_view(request, *args, **kwargs):  # *args, **kwargs
    update_list = Update.objects.all()
    context = {'update_list': update_list}
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "updates/index.html", context)
