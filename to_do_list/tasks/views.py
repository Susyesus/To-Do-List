from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/task_list.html", {"tasks": tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title:
            Task.objects.create(user=request.user, title=title, description=description)
            return redirect("task_list")
    return render(request, "tasks/add_task.html")

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect("task_list")

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect("task_list")
