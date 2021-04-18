from django.contrib import admin

# Register your models here.
from .models import Course, Content, Test, User, Homework

admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Test)
admin.site.register(User)
admin.site.register(Homework)
