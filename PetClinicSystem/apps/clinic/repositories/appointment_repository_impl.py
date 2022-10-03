from .appointment_repository import AppointmentRepository
from ..models import Appointment
from django.db.models import Q

class AppointmentRepositoryImpl(AppointmentRepository):
    def create(self, appointment):
        new_appointment = Appointment.objects.create(
            date=appointment['date'],
            description=appointment['description'],
            pet=appointment['pet'],
            veterinary=appointment['veterinary'],
            diagnosis=appointment['diagnosis']
        )
        for drug in appointment['drugs']:
            new_appointment.drugs.add(drug)

        return new_appointment

    def get_all(self, search):
        appointments = Appointment.objects.all()
        if search:
            appointments = appointments.filter(
                Q(pet__name__icontains=search) |
                Q(veterinary__name__icontains=search)
            )
        return appointments

    def delete(self, id):
        Appointment.objects.get(id=id).delete()

    def update(self, appointment):
        appointment_edited = Appointment.objects.filter(id=appointment['id']).update(
            date=appointment['date'],
            description=appointment['description'],
            pet=appointment['pet'],
            veterinary=appointment['veterinary'],
            diagnosis=appointment['diagnosis']
        )

        appointment_edited = Appointment.objects.get(id=appointment['id'])

        appointment_edited.drugs.clear()

        for drug in appointment['drugs']:
            appointment_edited.drugs.add(drug)

        return appointment_edited
    
    def get_by_id(self, id):
        return Appointment.objects.get(id=id)