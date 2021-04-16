from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path


def login_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "registration/login.html", {})
