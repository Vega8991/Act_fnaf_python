from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Animatronic, Party


class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned']
        labels = {
            'name': 'Name',
            'animal': 'Animal type',
            'build_date': 'Build date',
            'decommissioned': 'Decommissioned',
        }
        widgets = {
            'build_date': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'name': {
                'required': 'The name of the animatronic is required',
                'max_length': 'The name of the animatronic must not be more than 50 characters long',
            },
            'build_date': {
                'required': 'The build date is required',
            },
        }


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['name', 'attendants']
        labels = {
            'name': 'Parties',
            'attendants': 'Attendants',
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
