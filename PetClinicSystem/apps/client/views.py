from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .services.client_service import ClientService
from .repositories.client_repository_impl import ClientRepositoryImpl
from .repositories.address_repository_impl import AddressRepositoryImpl

from .services.pet_service import PetService
from .repositories.pet_repository_impl import PetRepositoryImpl

client_service = ClientService(
	client_repository=ClientRepositoryImpl(),
	address_repository=AddressRepositoryImpl()
)

pet_service = PetService(
	pet_repository=PetRepositoryImpl()
)

class ClientAddView(View):
	def get(self, request):
		client_form, address_form = client_service.client_form()
		return render(request, 'client/form.html', {'client_form': client_form, 'address_form': address_form, 'action': '/clients/'})

class ClientEditView(View):
	def get(self, request, id):
		client_form, address_form = client_service.client_form_edit(id)
		return render(request, 'client/form.html', {'client_form': client_form, 'address_form': address_form, 'action': f'/clients/edit/{id}/'})

	def post(self, request, id):
		client_service.update(request.POST, id)

		return redirect('/clients/')

class ClientDeleteView(View):
	def get(self, request, id):
		client_service.delete(id)

		return redirect('/clients/')

class ClientDetailView(View):
	def get(self, request, id):
		client = client_service.get_by_id(id)
		return render(request, 'client/detail.html', {'client': client})

class ClientView(View):
	def get(self, request):
		clients = client_service.get_all()
		return render(request, 'client/list.html', {'clients': clients})

	def post(self, request):
		client_service.create(request.POST)

		return redirect('clients')

class PetAddView(View):
	def get(self, request):
		pet_form = pet_service.pet_form()
		return render(request, 'pet/form.html', {'pet_form': pet_form, 'action': '/clients/pets/'})

class PetView(View):
	def get(self, request):
		pets = pet_service.get_all()
		return render(request, 'pet/list.html', {'pets': pets})

	def post(self, request):
		pet_service.create(request.POST)

		return redirect('pets')

class PetEditView(View):
	def get(self, request, id):
		pet_form = pet_service.pet_form_edit(id)
		return render(request, 'pet/form.html', {'pet_form': pet_form, 'action': f'/clients/pets/edit/{id}/'})

	def post(self, request, id):
		pet_service.update(request.POST, id)

		return redirect('/clients/pets/')

class PetDeleteView(View):
	def get(self, request, id):
		pet_service.delete(id)

		return redirect('/clients/pets/')