from abc import abstractmethod

class AppointmentRepository:
    @abstractmethod
    def create(self, appointment):
        pass

    @abstractmethod
    def get_all(self, search):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, appointment):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass