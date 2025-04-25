from django.shortcuts import render, redirect, get_object_or_404
from .models import Project

from collections import Counter
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.all().order_by('-start_date')

    # 상태별 개수 계산
    status_counts = Counter(projects.values_list('status', flat=True))
    total_projects = projects.count()

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'status_counts': status_counts,
        'total_projects': total_projects,
    })


def project_create(request):
    if request.method == 'POST':
        Project.objects.create(
            status=request.POST['status'],
            department=request.POST['department'],
            position=request.POST['position'],
            manager=request.POST['manager'],
            name=request.POST['name'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
        )
        return redirect('project_list')
    return render(request, 'projects/project_create.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_delete.html', {'project': project})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    status_choices = ["요청", "대기", "진행", "피드백", "완료", "보류"]

    if request.method == 'POST':
        project.name = request.POST['name']
        project.manager = request.POST['manager']
        project.department = request.POST['department']
        project.position = request.POST['position']
        project.status = request.POST['status']
        project.start_date = request.POST['start_date']
        project.end_date = request.POST['end_date']
        project.save()
        return redirect('project_detail', pk=pk)

    return render(request, 'projects/project_edit.html', {
        'project': project,
        'status_choices': status_choices
    })
