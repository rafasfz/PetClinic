from abc import abstractmethod

class AddressRepository:
    @abstractmethod
    def create(self, address):
        pass

    @abstractmethod
    def update(self, address):
        pass