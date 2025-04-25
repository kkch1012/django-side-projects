from django.db import models
from datetime import date, timedelta
import random

class Project(models.Model):
    STATUS_CHOICES = [
        ("요청", "요청"),
        ("대기", "대기"),
        ("진행", "진행"),
        ("피드백", "피드백"),
        ("완료", "완료"),
        ("보류", "보류"),
    ]

    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    progress_rate = models.IntegerField(default=0)  # 진행률 필드

    def __str__(self):
        return self.name

    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def working_days(self):
        count = 0
        for d in range(self.total_days()):
            current = self.start_date + timedelta(days=d)
            if current.weekday() < 5:  # 월~금만 카운트
                count += 1
        return count

    def calculate_progress_rate(self):
        if self.status in ["요청", "대기"]:
            return 0
        elif self.status in ["진행", "피드백"]:
            return random.randint(0, 80)
        else:  # 완료, 보류
            return 100

    def calculate_elapsed_percentage(self):
        total_duration = self.end_date - self.start_date
        elapsed_duration = date.today() - self.start_date
        if total_duration.days > 0:
            return min(100, (elapsed_duration.days / total_duration.days) * 100)
        return 0

    def save(self, *args, **kwargs):
        self.progress_rate = self.calculate_progress_rate()
        super(Project, self).save(*args, **kwargs)
