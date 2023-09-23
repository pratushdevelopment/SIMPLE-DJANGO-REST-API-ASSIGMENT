
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

