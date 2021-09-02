from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.models import MyUser

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    date_filed = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, related_name='created')
    status_choices = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('invalid', 'Invalid')
    ]
    status = models.CharField(max_length=100, choices=status_choices, default='New')
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='assigned')
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='completed')

    def __str__(self):
        return self.name