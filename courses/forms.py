from django import forms
from .models import HomeworkSubmission
from django.forms import ModelForm


class ModelFormWithFileField(forms.Form):
    submission_title = forms.CharField(max_length=50)
    submission_description = forms.CharField(widget=forms.Textarea)
    submission_file_upload = forms.FileField()


class NewHomeworkForm(forms.Form):
    homework_title = forms.CharField(max_length=200)
    homework_description = forms.CharField(max_length=200)
    homework_instruction = forms.CharField(widget=forms.Textarea)
    homework_due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )


class DocumentForm(ModelForm):
    submission_description = forms.CharField(
        widget=forms.Textarea, required=False)

    class Meta:
        model = HomeworkSubmission
        fields = ['submission_title', 'submission_description',
                  'submission_file_upload', ]
