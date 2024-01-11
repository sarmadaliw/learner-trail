from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("get_subject/", views.get_subject),
    path("topics/", views.all_topics),
    path("topic/", views.topic),
    path("new_topic/", views.new_topic),
    path("get_topic/", views.get_topic),
    path("get_entry/", views.get_entry),
    path("new_entry/", views.new_entry),
    path("edit_entry/", views.edit_entry),
]