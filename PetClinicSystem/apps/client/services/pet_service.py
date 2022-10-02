from dataclasses import dataclass
import datetime
from ..forms import PetForm
from ..repositories.pet_repository import PetRepository

@dataclass
class PetService():
    pet_repository: PetRepository
    
    def pet_form(self):
        pet_form = PetForm()
        return pet_form

    def create(self, request_post):
        pet_form = PetForm(request_post)
        if not pet_form.is_valid():
            raise Exception('Invalid pet form')
        pet = self.pet_repository.create(pet_form.cleaned_data)
        return pet

    def get_all(self):
        return self.pet_repository.get_all()

    def pet_form_edit(self, id):
        pet = self.pet_repository.get_by_id(id)
        pet_form = PetForm(instance=pet)
        return pet_form

    def update(self, request_post, id):
        pet_form = PetForm(request_post)
        if not pet_form.is_valid():
            raise Exception('Invalid pet form')
        pet_form.cleaned_data['id'] = id
        pet = self.pet_repository.update(pet_form.cleaned_data)
        return pet

    def delete(self, id):
        self.pet_repository.delete(id)

    
