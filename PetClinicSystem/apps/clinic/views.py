from django.shortcuts import redirect, render
from django.views import View
from django.shortcuts import render, redirect

from .services.drug_service import DrugService
from .repositories.drug_repository_impl import DrugRepositoryImpl

from .services.veterinary_service import VeterinaryService
from .repositories.veterinary_repository_impl import VeterinaryRepositoryImpl

drug_service = DrugService(
    drug_repository=DrugRepositoryImpl()
)

veterinary_service = VeterinaryService(
    veterinary_repository=VeterinaryRepositoryImpl()
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
        return render(request, 'veterinary/detail.html', {'veterinary': veterinary})