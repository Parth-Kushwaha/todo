from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TaskList
from . import forms 

# Create your views here.
@login_required
def home_view(request):
    items= TaskList.objects.all()
    return render(request, 'tasklist/home.html',context={"items":items})

@login_required
def task_create(request):
    form =forms.TaskForm()

    if request.method=='POST':
        form=forms.TaskForm(request.POST)

        if form.is_valid():
            submission=form.save(commit=False)
            submission.user=request.user
            submission.save()
            return redirect('home')

    return render(request, 'tasklist/task_form.html', context={'form':form})

@login_required
def task_change(request, task_id):
    task=get_object_or_404(TaskList, id=task_id)
    edit_form=forms.TaskForm(instance=task)

    if request.method=='POST':
        edit_form=forms.TaskForm(request.POST, instance=task)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    else:
        form= forms.TaskForm(instance=task)

    return render(request, 'tasklist/edit_task.html',context={'edit_form':edit_form})

@login_required
def task_delete(request,task_id): 
    task=get_object_or_404(TaskList,id=task_id)   
    if request.method=='POST':
        task.delete()
        return redirect('home')
    return render(request, 'tasklist/delete_confirm.html')
