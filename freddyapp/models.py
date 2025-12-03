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
    parties = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
