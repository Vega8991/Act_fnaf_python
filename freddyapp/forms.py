from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Animatronic, Party

# Formulario para crear/editar animatronicos
class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned']
        
        # Etiquetas de los campos
        labels = {
            'name': 'Name',
            'animal': 'Animal type',
            'build_date': 'Build date',
            'decommissioned': 'Decommissioned',
        }
        
        # Widgets para los campos
        widgets = {
            'build_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        # Mensajes de error
        error_messages = {
            'name': {
                'required': 'The name of the animatronic is required',
                'max_length': 'The name of the animatronic must not be more than 50 characters long',
            },
            'build_date': {
                'required': 'The build date is required',
            },
        }


# Formulario para las fiestas (inline en el formulario de animatronic)
class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['name', 'attendants']
        
        # Etiquetas
        labels = {
            'name': 'Parties',
            'attendants': 'Attendants',
        }
    
    # Los campos no son obligatorios
    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['attendants'].required = False


# Formset para las fiestas
from django.forms import inlineformset_factory

PartyFormSet = inlineformset_factory(
    Animatronic, 
    Party, 
    form=PartyForm,
    extra=2,  # mostrar 2 formularios vacios
    can_delete=False
)


# Formulario de registro
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
