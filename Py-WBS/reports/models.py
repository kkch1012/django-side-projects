# reports/models.py
from django.db import models
from django.utils import timezone
from projects.models import Project

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()  # 업무 내용
    today_result = models.TextField(null=True, blank=True)
    tomorrow_plan = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"업무 - {self.project.name} ({self.id})"

    def get_project_deadline(self):
        """선택된 프로젝트의 완료 기한을 가져옵니다"""
        return self.project.end_date

    def get_project_progress(self):
        """선택된 프로젝트의 진행률을 가져옵니다"""
        return self.project.progress_rate
