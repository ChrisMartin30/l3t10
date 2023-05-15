from django import forms
from django.forms import ModelForm
from .models import Event, Followers


class EventForm(ModelForm):
    """Creates a form for the user to fill in to create a new event.
    """
    class Meta:
        model = Event
        fields = ('Title', 'event_date', 'location', 'description')

        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }


class MailingForm(ModelForm):
    """Creates a form for a user to fill in when joining the mailing list.
    """
    class Meta:
        model = Followers
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }