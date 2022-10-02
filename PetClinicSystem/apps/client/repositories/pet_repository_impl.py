from abc import abstractmethod
from .pet_repository import PetRepository
from ..models import Pet

class PetRepositoryImpl(PetRepository):
    def get_all(self):
        pets = Pet.objects.all()
        return pets

    def get_by_id(self, id):
        pet = Pet.objects.get(id=id)
        return pet

    def create(self, pet):
        pet = Pet.objects.create(
            **pet
        )
        return pet

    def update(self, pet):
        pet = Pet.objects.filter(id=pet['id']).update(
            **pet
        )
        return pet
    
    def delete(self, id):
        Pet.objects.filter(id=id).delete()

