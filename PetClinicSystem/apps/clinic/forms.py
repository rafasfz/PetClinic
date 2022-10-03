from django.forms import ModelForm
from .models import Drug, Veterinary, Appointment

class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['name']

class VeterinaryForm(ModelForm):
    class Meta:
        model = Veterinary
        fields = ['name', 'email', 'phone']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'description', 'diagnosis', 'drugs', 'pet', 'veterinary']

