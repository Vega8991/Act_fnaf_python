from django.db import models

# Modelo para los animatronicos
class Animatronic(models.Model):
    # Opciones para el campo animal
    ANIMAL_CHOICES = [
        ('Be', 'Bear'),
        ('Ch', 'Chicken'),
        ('Bu', 'Bunny'),
        ('Fo', 'Fox'),
    ]
    
    # Campo nombre
    name = models.CharField(max_length=50)
    
    # Campo tipo de animal
    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    
    # Campo fecha de construccion
    build_date = models.DateField()
    
    # Campo si esta desactivado
    decommissioned = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


# Modelo para las fiestas
class Party(models.Model):
    # Relacion con animatronico
    animatronic = models.ForeignKey(Animatronic, on_delete=models.CASCADE, related_name='parties')
    
    # Nombre de la fiesta
    name = models.CharField(max_length=100, blank=True)
    
    # Numero de asistentes
    attendants = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
