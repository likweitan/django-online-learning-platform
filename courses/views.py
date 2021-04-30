from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.urls import path

from django.contrib.auth.decorators import login_required
from .models import Course, Homework, HomeworkSubmission, Test
from .forms import DocumentForm, NewHomeworkForm
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User


@login_required
def courses_view(request, *args, **kwargs):  # *args, **kwargs
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
    homework_list = Homework.objects.all().filter(
        course_id=course_id).order_by('-homework_updated_datetime')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewHomeworkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as requir
            homework_title = form.cleaned_data['homework_title']
            homework_description = form.cleaned_data['homework_description']
            homework_instruction = form.cleaned_data['homework_instruction']
            homework_due_date = form.cleaned_data['homework_due_date']
            homework = Homework(course_id=course_id, homework_title=homework_title,
                                homework_description=homework_description, homework_instruction=homework_instruction, homework_due_date=homework_due_date)
            homework.save()
            form = NewHomeworkForm()
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            context = {'course': course,
                       'homework_list': homework_list, 'form': form}
            return render(request, 'courses/homework.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewHomeworkForm()
    context = {'course': course, 'homework_list': homework_list, 'form': form}
    return render(request, 'courses/homework.html', context)


@login_required
def homework_submission_view(request, course_id, homework_id):
    course = get_object_or_404(Course, pk=course_id)
    homework = get_object_or_404(Homework, id=homework_id)
    if not request.user.is_staff:
        submission_list = HomeworkSubmission.objects.all().filter(
            homework_id=homework_id, user=request.user.id).order_by('-homework_submission_updated_datetime')
    else:
        submission_list = HomeworkSubmission.objects.all().filter(
            homework_id=homework_id).order_by('-homework_submission_updated_datetime')
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = DocumentForm(request.POST, request.FILES)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_id = User.objects.get(id=request.user.id)
            homework_id = Homework.objects.get(id=homework_id)
            form = form.save(commit=False)
            form.user = user_id
            form.homework = homework_id
            form.save()
            form = DocumentForm()
            context = {'course': course, 'homework': homework, 'form': form,
                       'submission_list': submission_list}
            # redirect to a new URL:
            return render(request, 'courses/submission.html', context)

    # If this is a GET (or any other method) create the default form.
    else:
        form = DocumentForm()

    context = {'course': course, 'homework': homework, 'form': form,
               'submission_list': submission_list}

    return render(request, 'courses/submission.html', context)


@login_required
def tests_view(request, course_id):  # *args, **kwargs
    test_list = Test.objects.all().filter(course=course_id)
    context = {'test_list': test_list}
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, 'tests/index.html', context)
