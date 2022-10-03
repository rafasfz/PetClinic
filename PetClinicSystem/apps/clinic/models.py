from tabnanny import verbose
from django.db import models

from client.models import Pet

class Veterinary(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    phone = models.CharField(max_length=255, verbose_name='Telefone')

    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField(verbose_name='Data')
    description = models.TextField(verbose_name='Descrição')
    diagnosis = models.TextField(verbose_name='Diagnóstico')
    drugs = models.ManyToManyField(Drug, verbose_name='Remédios')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Paciente')
    veterinary = models.ForeignKey(Veterinary, on_delete=models.CASCADE, related_name='appointments', verbose_name='Veterinário')

    def __str__(self):
        return self.description