from django import forms
from .models import HomeworkSubmission
from django.forms import ModelForm


class ModelFormWithFileField(forms.Form):
    submission_title = forms.CharField(max_length=50)
    submission_description = forms.CharField(widget=forms.Textarea)
    submission_file_upload = forms.FileField()


class DocumentForm(ModelForm):
    class Meta:
        model = HomeworkSubmission
        fields = ['submission_title', 'submission_description',
                  'submission_file_upload', ]
