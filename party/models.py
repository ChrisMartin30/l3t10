from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Followers(models.Model):
    """Database of people who are on mailing list.
    """
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Database of events.
class Event(models.Model):
    """Database of events that are available

    :param Title: The name of the Event
    :param event_date: The date of the Event
    :param location: The place of the event
    :param descritption: A description of the event
    :param attendees: People who are going to be at the event. 
    """
    Title = models.CharField('Event Name', max_length=150)
    event_date = models.DateTimeField('Date')
    location = models.CharField('Place', max_length=150)
    description = models.TextField('Description', max_length=900, blank=True)
    attendees = models.ManyToManyField(Followers, blank=True)

    def __str__(self):
        return self.Title
    
