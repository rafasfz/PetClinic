from abc import abstractmethod


class PetRepository:
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, pet):
        pass

    @abstractmethod
    def update(self, pet):
        pass

    @abstractmethod
    def delete(self, id):
        pass

