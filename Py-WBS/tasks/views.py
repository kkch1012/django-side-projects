from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from projects.models import Project

def task_list(request):
    project_id = request.GET.get('project')
    if project_id:
        tasks = Task.objects.filter(project__id=project_id)
    else:
        tasks = Task.objects.all()
    projects = Project.objects.all()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'projects': projects,
        'selected_project_id': project_id
    })

def task_create(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        Task.objects.create(
            project_id=request.POST['project'],
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            status=request.POST['status'],
            priority=request.POST['priority']
        )
        return redirect('task_list')
    return render(request, 'tasks/task_create.html', {'projects': projects})
