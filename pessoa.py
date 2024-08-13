from abc import ABC, abstractmethod
# A classe 'pessoa' herda de 'ABC', tornando-a uma classe abstrata 

class Pessoa(ABC):
    def __init__(self, nome: str):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @abstractmethod
    def __str__(self):
        pass
