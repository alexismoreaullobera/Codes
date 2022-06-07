from django.shortcuts import render
from listings.models import Topic
from django.http import HttpResponse

# Create your views here.

def topic (request) :
    topics = Topic.objects.all()
    return render (request, 'listings/topic.html', {'first_topic': topics[0]})
