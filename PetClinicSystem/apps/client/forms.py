from django.forms import ModelForm, DateField, SelectDateWidget
import datetime
from client.models import Client, Address, Pet

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('state', 'city', 'zip', 'district', 'street')
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 
class PetForm(ModelForm):
    birth_date = DateField(widget=SelectDateWidget(years=range(1900, datetime.date.today().year + 1)), initial=datetime.date.today, label='Data de nascimento')
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'birth_date', 'owner']
    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 