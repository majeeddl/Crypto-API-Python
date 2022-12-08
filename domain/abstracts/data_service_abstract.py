

from abc import ABC, abstractmethod, abstractproperty


class DataServicesAbstract(ABC):

    @property
    @abstractmethod
    def users(self):
        '''users property'''
        pass

    # @abstractproperty
    # def exchanges(self):
    #     '''exchanges property'''
    #     pass
