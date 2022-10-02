from django.forms import ModelForm
from .models import Client, Address

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('state', 'city', 'zip', 'district', 'street')

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']
