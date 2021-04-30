from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.urls import path

from django.contrib.auth.decorators import login_required
from .models import Course, Homework, HomeworkSubmission
from .forms import DocumentForm
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
    homework_list = Homework.objects.all().filter(course_id=course_id)
    context = {'course': course, 'homework_list': homework_list}
    return render(request, 'courses/homework.html', context)


@login_required
def homework_submission_view(request, course_id, homework_id):
    course = get_object_or_404(Course, pk=course_id)
    homework = get_object_or_404(Homework, id=homework_id)
    submission_list = HomeworkSubmission.objects.all().filter(
        homework_id=homework_id, user=request.user.id).order_by('-homework_submission_updated_datetime')
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
