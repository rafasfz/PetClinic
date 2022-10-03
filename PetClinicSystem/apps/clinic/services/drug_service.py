from dataclasses import dataclass
from ..forms import DrugForm
from ..repositories.drug_repository import DrugRepository


@dataclass
class DrugService:
    drug_repository: DrugRepository
    def get_all(self):
        drugs = self.drug_repository.get_all()
        return drugs

    def drug_form(self):
        drug_form = DrugForm()
        return drug_form

    def create(self, request_post):
        drug_form = DrugForm(request_post)
        if not drug_form.is_valid():
            raise Exception('Invalid drug form')
        drug = self.drug_repository.create(drug_form.cleaned_data)
        return drug

    def delete(self, id):
        self.drug_repository.delete(id)
