from django import forms
from django.forms import ModelForm
from .models import Event, Followers


# Create a form for a new event
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('Title', 'event_date', 'location', 'description')

        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }


# Create a form for joining the mailing list
class MailingForm(ModelForm):
    class Meta:
        model = Followers
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }