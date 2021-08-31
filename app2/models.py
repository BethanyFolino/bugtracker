from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.models import MyUser

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    date_filed = models.DateTimeField()
    description = models.models.TextField()
    filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status_choices = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]
    status = models.CharField(choices=status_choices, default='New')
    assigned_to = models.ForeignKey(None)
    completed_by = models.ForeignKey(None)