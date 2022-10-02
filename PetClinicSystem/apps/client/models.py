from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name='Rua')
    district = models.CharField(max_length=255, verbose_name='Bairro')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    state = models.CharField(max_length=255, verbose_name='Estado')
    zip = models.CharField(max_length=9, verbose_name='CEP')

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    phone = models.CharField(max_length=255, verbose_name='Telefone')
    email = models.CharField(max_length=255, verbose_name='Email')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='Endereço')

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    breed = models.CharField(max_length=255, verbose_name='Raça')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='pets', verbose_name='Dono')

    def __str__(self):
        return self.name