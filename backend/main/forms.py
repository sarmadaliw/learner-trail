from django import forms
from .models import Subject, Topic, Entry

class SubjectForm(forms.ModelForm):
    model = Subject
    fields = ["name"]
    labels = {"name": ""}

class TopicForm(forms.ModelForm):
    model = Topic
    fields = ["description"]
    labels = {"description": ""}

class EntryForm(forms.ModelForm):
    model = Entry
    fields = ["text"]
    labels = {"text": ""}
    widgets = {'text': forms.Textarea(attrs={'cols': 80})}