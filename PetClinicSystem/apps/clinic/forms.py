from django.forms import ModelForm, DateField, SelectDateWidget
from clinic.models import Drug, Veterinary, Appointment
import datetime

class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(DrugForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   
class VeterinaryForm(ModelForm):
    class Meta:
        model = Veterinary
        fields = ['name', 'email', 'phone']
    def __init__(self, *args, **kwargs):
        super(VeterinaryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 
class AppointmentForm(ModelForm):
    
    date = DateField(widget=SelectDateWidget(years=range(datetime.date.today().year, datetime.date.today().year + 2)), initial=datetime.date.today, label='Data do atendimento')
    class Meta:
        model = Appointment
        fields = ['date', 'description', 'diagnosis', 'drugs', 'pet', 'veterinary']
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 
