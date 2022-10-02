from abc import abstractmethod


class ClientRepository:
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, client, address):
        pass

    @abstractmethod
    def update(self, client, address):
        pass

