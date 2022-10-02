from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .services.client_service import ClientService
from .repositories.client_repository_impl import ClientRepositoryImpl
from .repositories.address_repository_impl import AddressRepositoryImpl

client_service = ClientService(
	client_repository=ClientRepositoryImpl(),
	address_repository=AddressRepositoryImpl()
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
