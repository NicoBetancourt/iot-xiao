from abc import ABC, abstractmethod 

class BaseController(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
