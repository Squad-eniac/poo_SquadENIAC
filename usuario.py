from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome: str, telefone: str, nacionalidade: str):
        super().__init__(nome)
        self.__telefone = telefone
        self.__nacionalidade = nacionalidade
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
    
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade
    
    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}'
