from dataclasses import dataclass

from ..repositories.appointment_repository import AppointmentRepository
from ..forms import AppointmentForm

@dataclass
class AppointmentService:
    appointment_repository: AppointmentRepository

    def get_all(self, search):
        return self.appointment_repository.get_all(search)

    def appointment_form(self):
        appointment_form = AppointmentForm()
        return appointment_form
    
    def appointment_form_edit(self, id):
        appointment = self.appointment_repository.get_by_id(id)
        appointment_form = AppointmentForm(instance=appointment)
        return appointment_form

    def create(self, request_post):
        appointment_form = AppointmentForm(request_post)
        if not appointment_form.is_valid():
            raise Exception('Invalid appointment form')
        appointment = self.appointment_repository.create(appointment_form.cleaned_data)
        return appointment

    def update(self, request_post, id):
        appointment_form = AppointmentForm(request_post)
        if not appointment_form.is_valid():
            raise Exception('Invalid appointment form')
        appointment_form.cleaned_data['id'] = id
        appointment = self.appointment_repository.update(appointment_form.cleaned_data)
        return appointment

    def get_by_id(self, id):
        appointment = self.appointment_repository.get_by_id(id)
        return appointment