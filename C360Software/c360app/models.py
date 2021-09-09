from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=100)
   
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()

    def __str__(self):
        return self.name