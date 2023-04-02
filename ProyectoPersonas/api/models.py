from django.db import models

# Create your models here.


class Persona(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.PositiveIntegerField()