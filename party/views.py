from django.shortcuts import render
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Followers
from .forms import EventForm, MailingForm


# Create your views here.

def home(request):
    """Returns the file home.html 
    """
    return render(request, 'home.html', {},)


# Creates a list of events in database and orders them by date
def events(request):
    event_list = Event.objects.all().order_by('event_date')

    return render(request, 'events.html', {'event_list': event_list})


# Adds event to the database
def add_event(request):
    """Adds an event to the events database using the EventForm.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event')
    else:
        form = EventForm
    
    return render(request, 'add_event.html', {'form': form},)


def mailing_list(request):
    """Adds details from a completed form to the mailing list database.
    """
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mailing_list')
    else:
        form = MailingForm
    
    return render(request, 'mailing_list.html', {'form': form},)

# Create a "view information about those who have signed up for the mailing list" option.
def view_mailing_list(request):
    """Creates a 'view mailing list' html file with a list of current users.
    """
    mailing_list_members = Followers.objects.all()

    return render(request, 'view_mailing_list.html', {'subscribers': mailing_list_members})