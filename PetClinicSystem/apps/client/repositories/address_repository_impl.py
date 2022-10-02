from .address_repository import AddressRepository
from ..models import Address

class AddressRepositoryImpl(AddressRepository):
    def create(self, address):
        address = Address.objects.create(
            **address
        )
        return address

    def update(self, address):
        address = Address.objects.filter(id=address['id']).update(
            **address
        )
        return address