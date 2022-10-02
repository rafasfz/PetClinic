from unicodedata import name
from django.forms import ModelForm, DateField, SelectDateWidget
import datetime
from .models import Client, Address, Pet

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('state', 'city', 'zip', 'district', 'street')

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']

class PetForm(ModelForm):
    birth_date = DateField(widget=SelectDateWidget(years=range(1900, datetime.date.today().year + 1)), initial=datetime.date.today, label='Data de nascimento')
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'birth_date', 'owner']
