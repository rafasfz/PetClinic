from .drug_repository import DrugRepository
from ..models import Drug

class DrugRepositoryImpl(DrugRepository):
    def get_all(self):
        drugs = Drug.objects.all()
        return drugs

    def create(self, drug):
        drug = Drug.objects.create(
            **drug
        )
        return drug

    def delete(self, id):
        Drug.objects.filter(id=id).delete()
