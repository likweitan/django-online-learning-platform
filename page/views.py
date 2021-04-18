from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path

from django.contrib.auth.decorators import login_required


@login_required
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})
