from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class StudyProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    customer = models.CharField(max_length=100, default="empty")
    executor = models.CharField(max_length=100, default="empty")

    date_created = models.DateTimeField(default=timezone.now)
    date_deadline = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    result = models.CharField(max_length=100, default="empty")

    # For querying convenience.
    def __str__(self):
        return self.title
