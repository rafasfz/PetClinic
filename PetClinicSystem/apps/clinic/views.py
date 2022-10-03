from django.shortcuts import redirect, render
from django.views import View
from django.shortcuts import render, redirect

from .services.appointment_service import AppointmentService

from .services.drug_service import DrugService
from .repositories.drug_repository_impl import DrugRepositoryImpl

from .services.veterinary_service import VeterinaryService
from .repositories.veterinary_repository_impl import VeterinaryRepositoryImpl


from .repositories.appointment_repository_impl import AppointmentRepositoryImpl

drug_service = DrugService(
    drug_repository=DrugRepositoryImpl()
)

veterinary_service = VeterinaryService(
    veterinary_repository=VeterinaryRepositoryImpl()
)

appointment_service = AppointmentService(
    appointment_repository=AppointmentRepositoryImpl(),
)

class DrugAddView(View):
    def get(self, request):
        drug_form = drug_service.drug_form()
        return render(request, 'drug/form.html', {'drug_form': drug_form, 'action': '/clinic/drugs/'})

class DrugDeleteView(View):
    def get(self, request, id):
        drug_service.delete(id)

        return redirect('/clinic/drugs/')

class DrugView(View):
    def get(self, request):
        drugs = drug_service.get_all()
        return render(request, 'drug/list.html', {'drugs': drugs})

    def post(self, request):
        drug_service.create(request.POST)

        return redirect('drugs')

class VeterinaryAddView(View):
    def get(self, request):
        veterinary_form = veterinary_service.veterinary_form()
        return render(request, 'veterinary/form.html', {'veterinary_form': veterinary_form, 'action': '/clinic/veterinaries/'})

class VeterinaryView(View):
    def get(self, request):
        veterinaries = veterinary_service.get_all()
        return render(request, 'veterinary/list.html', {'veterinaries': veterinaries})

    def post(self, request):
        veterinary_service.create(request.POST)

        return redirect('veterinaries')

class VeterinaryDeleteView(View):
    def get(self, request, id):
        veterinary_service.delete(id)
        return redirect('/clinic/veterinaries/')

class VeterinaryEditView(View):
    def get(self, request, id):
        veterinary_form = veterinary_service.veterinary_form_edit(id)
        return render(request, 'veterinary/form.html', {'veterinary_form': veterinary_form, 'action': '/clinic/veterinaries/edit/%s/' % id})

    def post(self, request, id):
        veterinary_service.update(request.POST, id)

        return redirect('veterinaries')

class VeterinaryDetailView(View):
    def get(self, request, id):
        veterinary = veterinary_service.get_by_id(id)
        appointments = veterinary.appointments.all()
        return render(request, 'veterinary/detail.html', {'veterinary': veterinary, 'appointments': appointments})

class AppointmentAddView(View):
    def get(self, request):
        appointment_form = appointment_service.appointment_form()
        return render(request, 'appointment/form.html', {'appointment_form': appointment_form, 'action': '/clinic/appointments/'})

class AppointmentView(View):
    def get(self, request):
        search = request.GET.get('search', '')
        appointments = appointment_service.get_all(search)
        return render(request, 'appointment/list.html', {'appointments': appointments, 'search': search})

    def post(self, request):
        appointment_service.create(request.POST)

        return redirect('appointments')

class AppointmentEditView(View):
    def get(self, request, id):
        appointment_form = appointment_service.appointment_form_edit(id)
        return render(request, 'appointment/form.html', {'appointment_form': appointment_form, 'action': '/clinic/appointments/edit/%s/' % id})

    def post(self, request, id):
        appointment_service.update(request.POST, id)

        return redirect('appointments')

class AppointmentDetailView(View):
    def get(self, request, id):
        appointment = appointment_service.get_by_id(id)
        drugs = appointment.drugs.all()
        return render(request, 'appointment/detail.html', {'appointment': appointment, 'drugs': drugs})

