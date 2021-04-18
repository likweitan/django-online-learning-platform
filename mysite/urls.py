"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from page.views import home_view
from courses.views import courses_view, course_view, homeworks_view, homework_submission_view
from user.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('user/', include('user.urls')),
    path('', home_view, name='home'),
    path('courses/', courses_view, name='courses'),
    path('courses/<int:course_id>/', course_view, name='course'),
    path('courses/<int:course_id>/homework/',
         homeworks_view, name='homeworks'),
    path('courses/<int:course_id>/homework/<int:homework_id>/',
         homework_submission_view, name='homework_submission'),
]

# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
