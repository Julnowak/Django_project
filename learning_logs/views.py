from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """ Main Page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Topics page for Learning Log"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Shows topic and all entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Add new topic"""
    if request.method != "POST":
        # No data, empty form
        form = TopicForm()
    else:
        # data by POST, to work with
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Showing empty form
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request, topic_id):
    """ Add new entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # No data, empty form
        form = EntryForm()
    else:
        # data by POST, to work with
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    # Showing empty form
    context = {'topic': topic,'form': form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request, entry_id):
    """ Edit entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != "POST":
        # No changes, user can  see text
        form = EntryForm(instance=entry)
    else:
        # data by POST, to work with
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    # Showing empty form
    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request,'learning_logs/edit_entry.html',context)