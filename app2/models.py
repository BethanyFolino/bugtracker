from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.models import MyUser

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    date_filed = models.DateTimeField()
    description = models.TextField()
    filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='created')
    status_choices = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('invalid', 'Invalid')
    ]
    status = models.CharField(max_length=100, choices=status_choices, default='New')
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None, related_name='assigned')
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None, related_name='completed')