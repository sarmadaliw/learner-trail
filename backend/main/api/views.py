from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Subject, Topic, Entry
from .serializers import SubjectSerializer, TopicSerializer, EntrySerializer
from django.shortcuts import get_object_or_404

# Create your views here.

# Home page
@api_view(["GET"])
def home(request):
    """The home page of LearnerTrail"""
    data = {
        "app_name": "LearnerTrackr",
        "menu_options": ["Create Subject", "Create Topic", "Create Entry"],
    }
    return Response(data)

# Subject api
@api_view(["GET", "POST"])
def get_subject(request):
    """Retrieve and create a subject."""
    if request.method == "GET":
        items = Subject.objects.all()
        serializer = SubjectSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
# Topic api
@api_view(["GET", "POST"])
def get_topic(request):
    """Retrieve and create a topic."""
    if request.method == "GET":
        items = Topic.objects.all()
        serializer = TopicSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(["GET"])
def all_topics(request):
    """Retrieve all topics."""
    topics = Topic.objects.order_by("created")
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def topic(request, topic_id):
    """Retrieve a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by("created")
    topic_serializer = TopicSerializer(topic)
    entry_serializer = EntrySerializer(entries, many=True)
    data = {"topic": topic_serializer.data, "entries": entry_serializer.data}
    return Response(data)

@api_view(["POST"])
def new_topic(request):
    """Add a new topic."""
    if request.method == "POST":
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
    else:
        serializer = TopicSerializer()
    return Response(serializer.data)

# Entry api
@api_view(["GET", "POST"])
def get_entry(request):
    """Retreive enteries."""
    if request.method == "GET":
        items = Entry.objects.all()
        serializer = EntrySerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(["POST"])
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == "POST":
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(topic=topic)
            return Response(serializer.data)
    else:
        serializer = EntrySerializer()
    return Response(serializer.data)

@api_view(["POST"])
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == "POST":
        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        serializer = EntrySerializer(instance=entry)
    return Response(serializer.data)