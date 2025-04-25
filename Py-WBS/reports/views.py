from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Report
from projects.models import Project
from django.utils.dateparse import parse_date

def report_list(request):
    projects = Project.objects.all()
    selected_project_id = request.GET.get('project')  # ''일 수도 있음
    selected_date = request.GET.get('date')  # ''일 수도 있음

    reports = Report.objects.all()

    if selected_project_id:  # 프로젝트가 선택되었을 때만 필터링
        reports = reports.filter(project_id=selected_project_id)

    if selected_date:  # 날짜가 선택되었을 때만 필터링
        reports = reports.filter(date_created__date=parse_date(selected_date))

    today = timezone.now().date().isoformat()

    return render(request, 'reports/report_list.html', {
        'projects': projects,
        'reports': reports,
        'selected_project_id': selected_project_id,
        'selected_date': selected_date,
        'today': today,
    })


def report_create(request):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=request.POST['project'])
        date_str = request.POST.get('date_created')
        work_type = request.POST.get('work_type')
        content = request.POST.get('content')

        date_created = datetime.strptime(date_str, "%Y-%m-%d") if date_str else timezone.now()

        Report.objects.create(
            project=project,
            date_created=date_created,
            today_result=content if work_type == 'today' else '',
            tomorrow_plan=content if work_type == 'tomorrow' else '',
            description=""
        )
        return redirect('report_list')

    projects = Project.objects.all()
    today = timezone.now().date().isoformat()
    return render(request, 'reports/report_create.html', {
        'projects': projects,
        'today': today
    })

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    projects = Project.objects.all()

    if request.method == 'POST':
        report.project = get_object_or_404(Project, pk=request.POST['project'])
        report.date_created = request.POST.get('date_created')
        report.today_result = request.POST.get('today_result', '')
        report.tomorrow_plan = request.POST.get('tomorrow_plan', '')
        report.save()
        return redirect('report_list')

    return render(request, 'reports/report_edit.html', {
        'report': report,
        'projects': projects
    })

def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    return redirect('report_list')

def get_project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    data = {
        'project_name': project.name,
        'end_date': project.end_date,
        'progress_rate': project.progress_rate,
    }
    return JsonResponse(data)