from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.urls import path

from django.contrib.auth.decorators import login_required
from .models import Course, Homework


@login_required
def courses_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, 'courses/index.html', context)


@login_required
def course_view(request, course_id):
    #course_list = Course.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'courses/course.html', context)


@login_required
def homeworks_view(request, course_id):
    #course_list = Course.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    homework_list = Homework.objects.all().filter(course_id=course_id)
    context = {'course': course, 'homework_list': homework_list}
    return render(request, 'courses/homework.html', context)


@login_required
def homework_submission_view(request, course_id, homework_id):
    #course_list = Course.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    homework = get_object_or_404(Homework, pk=homework_id)
    context = {'course': course, 'homework': homework}
    return render(request, 'courses/submission.html', context)
