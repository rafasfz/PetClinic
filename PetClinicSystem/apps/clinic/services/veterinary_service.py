from dataclasses import dataclass

from ..repositories.veterinary_repository import VeterinaryRepository
from ..forms import VeterinaryForm

@dataclass
class VeterinaryService():
    veterinary_repository: VeterinaryRepository

    def veterinary_form(self):
        veterinary_form = VeterinaryForm()
        return veterinary_form

    def create(self, request_post):
        veterinary_form = VeterinaryForm(request_post)
        if not veterinary_form.is_valid():
            raise Exception('Invalid veterinary form')
        veterinary = self.veterinary_repository.create(veterinary_form.cleaned_data)
        return veterinary

    def get_all(self):
        return self.veterinary_repository.get_all()

    def delete(self, id):
        self.veterinary_repository.delete(id)

    def veterinary_form_edit(self, id):
        veterinary = self.veterinary_repository.get_by_id(id)
        veterinary_form = VeterinaryForm(instance=veterinary)
        return veterinary_form

    def update(self, request_post, id):
        veterinary_form = VeterinaryForm(request_post)
        if not veterinary_form.is_valid():
            raise Exception('Invalid veterinary form')
        veterinary_form.cleaned_data['id'] = id
        veterinary = self.veterinary_repository.update(veterinary_form.cleaned_data)
        return veterinary

    def get_by_id(self, id):
        veterinary = self.veterinary_repository.get_by_id(id)
        return veterinary