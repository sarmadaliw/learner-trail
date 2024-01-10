from django import forms
from .models import Subject, Topic, Entry

class SubjectForm(forms.ModelForm):
    model = Subject
    fields = ["text"]
    labels = {"text": ""}

class TopicForm(forms.ModelForm):
    model = Topic
    fields = ["text"]
    labels = {"text": ""}

class EntryForm(forms.ModelForm):
    model = Entry
    fields = ["text"]
    labels = {"text": ""}
    widgets = {'text': forms.Textarea(attrs={'cols': 80})}