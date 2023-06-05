from django.shortcuts import render

# Create your views here.
def index(request):
    """ Main Page for Learning Log"""
    return render(request, 'learning_logs/index.html')