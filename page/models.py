from django.db import models

from django.conf import settings

from courses.models import Course

# Create your models here.


class Update(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    update_title = models.CharField(max_length=200)
    update_description = models.TextField()
    #course_icon = models.CharField(max_length=200)
    update_created_datetime = models.DateTimeField(auto_now_add=True)
