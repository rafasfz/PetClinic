from abc import abstractmethod


class VeterinaryRepository:
    @abstractmethod
    def create(self, veterinary):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, veterinary):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass