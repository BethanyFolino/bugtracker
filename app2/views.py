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
from django.contrib import messages

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
    ticket_created = Ticket.objects.filter(filed_by=my_user)
    ticket_assigned = Ticket.objects.filter(assigned_to=my_user)
    ticket_completed = Ticket.objects.filter(completed_by=my_user)
    return render(request, 'user_detail.html', {'my_user': my_user, 'ticket_created': ticket_created, 'ticket_assigned': ticket_assigned, 'ticket_completed': ticket_completed})

def add_ticket(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                filed_by=request.user,
                description=data['description'],
            )
            messages.success(request, 'Ticket successfully created!', extra_tags='success')
            return HttpResponseRedirect(reverse('home'))
    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

def edit_ticket(request, id):
    item = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item.title = data['title']
            item.description = data['description']
            item.save()
            messages.success(request, 'Ticket successfully edited!', extra_tags='success')
            return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

    form = EditTicketForm(initial={
        'title': item.title,
        'description': item.description
    })
    return render(request, 'generic_form.html', {'form': form})

def assign_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    messages.success(request, 'Ticket successfully assigned!', extra_tags='success')
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

def complete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.completed_by = ticket.assigned_to
    ticket.status = 'Done'
    ticket.assigned_to = None
    ticket.save()
    messages.success(request, 'Ticket successfully marked as completed!', extra_tags='success')
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

def invalid_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'Invalid'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    messages.success(request, 'Ticket successfully marked as invalid!', extra_tags='success')
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

