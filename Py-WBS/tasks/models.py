from django.db import models
from projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', '미완료'),
        ('doing', '진행중'),
        ('done', '완료'),
    ]
    PRIORITY_CHOICES = [
        ('high', '상'),
        ('medium', '중'),
        ('low', '하'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return f"[{self.project.name}] {self.title}"
