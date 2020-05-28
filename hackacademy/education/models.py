from django.db import models
from django.utils import timezone
import requests


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    name = models.CharField(max_length=250)
    week = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class Solutions(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    url = models.URLField()

    def save(self, *args, **kwargs):
        # if self.url.count("https://www.github.com/") > 0:
        try:
            r = requests.get(self.url, timeout=5)
            if r.status_code == 200:
                super().save(*args, **kwargs)
        except Exception as e:
            raise e
