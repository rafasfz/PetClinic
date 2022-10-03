from .veterinary_repository import VeterinaryRepository
from ..models import Veterinary

class VeterinaryRepositoryImpl(VeterinaryRepository):
    def create(self, veterinary):
        Veterinary.objects.create(**veterinary)

    def get_all(self):
        return Veterinary.objects.all()

    def delete(self, id):
        Veterinary.objects.get(id=id).delete()

    def update(self, veterinary):
        Veterinary.objects.filter(id=veterinary['id']).update(**veterinary)
    
    def get_by_id(self, id):
        return Veterinary.objects.get(id=id)