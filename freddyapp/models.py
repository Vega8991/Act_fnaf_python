from django.db import models

class Animatronic(models.Model):
    ANIMAL_CHOICES = [
        ('Be', 'Bear'),
        ('Ch', 'Chicken'),
        ('Bu', 'Bunny'),
        ('Fo', 'Fox'),
    ]
    
    name = models.CharField(max_length=50)
    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    build_date = models.DateField()
    decommissioned = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Party(models.Model):
    animatronic = models.ForeignKey(Animatronic, on_delete=models.CASCADE, related_name='parties')
    name = models.CharField(max_length=100, blank=True)
    attendants = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
