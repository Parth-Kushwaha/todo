from django.shortcuts import render
from .models import TaskList
# Create your views here.

def home_view(request):
    items= TaskList.objects.all()
    return render(request, 'tasklist/home.html',context={"items":items})