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

@login_required
def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

@login_required
def user_detail(request, id):
    my_user = MyUser.objects.get(id=id)
    ticket_created = Ticket.objects.filter(filed_by=my_user)
    ticket_assigned = Ticket.objects.filter(assigned_to=my_user)
    ticket_finished = Ticket.objects.filter(completed_by=my_user)
    return render(request, 'user_detail.html', {'my_user': my_user, 'ticket_created': ticket_created, 'ticket_assigned': ticket_assigned, 'ticket_finished': ticket_finished})

@login_required
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
            return HttpResponseRedirect(reverse('home'))
    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def edit_ticket(request, id):
    item = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item.title = data['title']
            item.description = data['description']
            item.save()
            return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

    form = EditTicketForm(initial={
        'title': item.title,
        'description': item.description
    })
    return render(request, 'generic_form.html', {'form': form})

@login_required
def assign_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

@login_required
def finish_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.completed_by = ticket.assigned_to
    ticket.status = 'Done'
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

@login_required
def invalid_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'Invalid'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(id,)))

