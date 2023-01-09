

from abc import ABC, abstractmethod, abstractproperty


class ExchangeServiceAbstract(ABC):


    @property
    @abstractmethod
    def fetchBalance():
        '''fectch balance'''
        pass


    @property
    @abstractmethod
    def fetchAccounts():
        '''fetch accounts'''
        pass

