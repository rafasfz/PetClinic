from dataclasses import dataclass

from ..forms import ClientForm, AddressForm

from ..repositories.client_repository import ClientRepository
from ..repositories.address_repository import AddressRepository

@dataclass
class ClientService():
    client_repository: ClientRepository
    address_repository: AddressRepository

    def get_all(self):
        return self.client_repository.get_all()

    def client_form(self):
        client_form = ClientForm()
        address_form = AddressForm()
        return client_form, address_form

    def client_form_edit(self, id):
        client = self.client_repository.get_by_id(id)
        client_form = ClientForm(instance=client)
        address_form = AddressForm(instance=client.address)
        return client_form, address_form

    def create(self, request_post):
        client_form = ClientForm(request_post)
        address_form = AddressForm(request_post)

        if not (client_form.is_valid() and address_form.is_valid()):
            raise Exception('Invalid client and address form')

        address = self.address_repository.create(address_form.cleaned_data)
        client = self.client_repository.create(client_form.cleaned_data, address)

        return client, address
    
    def update(self, request_post, id):
        client_form = ClientForm(request_post)
        address_form = AddressForm(request_post)

        if not (client_form.is_valid() and address_form.is_valid()):
            raise Exception('Invalid client and address form')

        client_data = self.client_repository.get_by_id(id)
        client_form.cleaned_data['id'] = id
        address_form.cleaned_data['id'] = client_data.address.id

        address = self.address_repository.update(address_form.cleaned_data)
        client = self.client_repository.update(client_form.cleaned_data, address)

        return client, address

    def get_by_id(self, id):
        client = self.client_repository.get_by_id(id)
        return client

    def delete(self, id):
        client = self.client_repository.get_by_id(id)
        client.delete()
        return client
