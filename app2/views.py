from django.shortcuts import render, HttpResponseRedirect, reverse
from app1.models import MyUser
from app2.forms import AddTicketForm, EditTicketForm
from app2.models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from bugtracker.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
@login_required
def homepage(request):
    tickets = Ticket.objects.all()
    return render(request, 'homepage.html', {'tickets': tickets})

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

def user_detail(request, id):
    my_user = MyUser.objects.get(id=id)
    return render(request, 'user_detail.html', {'my_user': my_user})

def add_ticket(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                date_filed=data['date_filed'],
                description=data['description'],
                filed_by=data['filed_by'],
                status=data['status'],
                assigned_to=data['assigned_to'],
                completed_by=data['completed_by']
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

def edit_ticket(request, ticket_id):
    item = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ...
    form = EditTicketForm(initial={
        'title': item.title,
        'description': item.description
    })
    return render(request, 'generic_form.html', {'form': form})


def assigned_ticket(request):
    ...

def completed_ticket(request):
    ...

def invalid_ticket(request):
    ...

