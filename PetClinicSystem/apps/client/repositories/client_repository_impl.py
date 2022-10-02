from .client_repository import ClientRepository
from ..models import Client

class ClientRepositoryImpl(ClientRepository):
    def get_all(self):
        clients = Client.objects.all()
        return clients

    def create(self, client, address):
        client = Client.objects.create(
            **client,
            address=address
        )
        return client

    def get_by_id(self, id):
        client = Client.objects.get(id=id)
        return client

    def update(self, client, address):
        client = Client.objects.filter(id=client['id']).update(
            **client,
            address=address
        )
        return client