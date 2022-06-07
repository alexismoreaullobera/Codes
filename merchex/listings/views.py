from django.shortcuts import render
from listings.models import Topic
from django.http import HttpResponse

# Create your views here.

def topic_list (request) :
    topics = Topic.objects.all()
    return render (request, 'listings/topic_list.html', {'topics': topics})

def topic_details (request, id):
    topic = Topic.objects.get(id=id)
    return render (request, 'listings/topic_details.html', {'topic' : topic})
