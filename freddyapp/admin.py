from django.contrib import admin
from .models import Animatronic, Party

# Registrar los modelos en el admin
admin.site.register(Animatronic)
admin.site.register(Party)
