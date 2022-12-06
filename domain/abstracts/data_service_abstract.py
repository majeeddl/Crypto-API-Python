

from abc import ABC, abstractmethod, abstractproperty


class DataServiceAbstract(ABC):

    # @abstractmethod
    @abstractproperty
    def users(self):
        pass
