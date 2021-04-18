from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=200)
    #course_icon = models.CharField(max_length=200)
    course_created_datetime = models.DateTimeField(auto_now_add=True)


class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=200)
    content_description = models.CharField(max_length=200)
    content_created_datetime = models.DateTimeField(auto_now_add=True)
    content_updated_datetime = models.DateTimeField(auto_now=True)


class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    homework_title = models.CharField(max_length=200)
    homework_description = models.CharField(max_length=200)
    homework_instruction = models.TextField()
    homework_due_datetime = models.DateTimeField(null=True)
    homework_created_datetime = models.DateTimeField(auto_now_add=True)
    homework_updated_datetime = models.DateTimeField(auto_now=True)


class HomeworkSubmission(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    homework = models.ForeignKey(Course, on_delete=models.CASCADE)
    submission_title = models.CharField(max_length=200)
    submission_description = models.CharField(max_length=200)
    submission_file_upload = models.FileField(upload_to='documents/')
    homework_submission_updated_datetime = models.DateTimeField(
        auto_now_add=True)


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test_title = models.CharField(max_length=200)
    test_description = models.CharField(max_length=200)
    test_due_date = models.DateField()
    content_created_datetime = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    instructor = models.BooleanField(default=False)
    user_created_datetime = models.DateTimeField(auto_now_add=True)
    user_updated_datetime = models.DateTimeField(auto_now=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     instructor = models.BooleanField(default=False)
#     user_created_datetime = models.DateTimeField(auto_now_add=True)
#     user_updated_datetime = models.DateTimeField(auto_now=True)
