from abc import abstractmethod

class DrugRepository:
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, drug):
        pass

    @abstractmethod
    def delete(self, id):
        pass