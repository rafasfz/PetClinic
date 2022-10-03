from django.forms import ModelForm, DateField, SelectDateWidget
from .models import Drug, Veterinary, Appointment
import datetime

class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['name']

class VeterinaryForm(ModelForm):
    class Meta:
        model = Veterinary
        fields = ['name', 'email', 'phone']

class AppointmentForm(ModelForm):
    
    date = DateField(widget=SelectDateWidget(years=range(datetime.date.today().year, datetime.date.today().year + 2)), initial=datetime.date.today, label='Data do atendimento')
    class Meta:
        model = Appointment
        fields = ['date', 'description', 'diagnosis', 'drugs', 'pet', 'veterinary']

