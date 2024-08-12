from exemplar import Exemplar
from usuario import Usuario
from datetime import datetime

class Emprestimo:
    def __init__(self, usuario, exemplar, dataEmprestimo = None):
        self.usuario = usuario
        self.exemplar = exemplar
        self.exemplar.emprestar()
        self.status = 'Emprestado'
        self.dataEmprestimo = dataEmprestimo
        self.__dataDevolucao = None

    @property
    def exemplar(self):
        return self.__exemplar
    
    @exemplar.setter
    def exemplar(self, exemplar):
        if isinstance(exemplar, Exemplar):
            self.__exemplar = exemplar
        else:
            raise TypeError(f'Erro! Não foi possível definir o exemplar. O exemplar deve ser uma instância da classe Exemplar e não {type(exemplar)}')
    
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        else:
            raise TypeError(f'Erro! Não foi possível definir o usuário. O usuário deve ser uma instância da classe Usuario e não {type(usuario)}')
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):    
        if isinstance(status, str):
            status = status.lower().capitalize()
            if status in ['Emprestado', 'Devolvido']:
                self.__status = status
            else:
                raise ValueError(f'Erro! O status deve ser "Emprestado" ou "Devolvido"')
        else:
            raise TypeError(f'Erro! Não foi possível definir o status. O status deve ser uma string e não {type(status)}')
    
    @property
    def dataEmprestimo(self):
        return self.__dataEmprestimo
    
    @dataEmprestimo.setter
    def dataEmprestimo(self, dataEmprestimo):
        if dataEmprestimo is None: 
            dataEmprestimo = datetime.now()
        else:
            try:
                dataEmprestimo = datetime.strptime(dataEmprestimo, '%d/%m/%Y')
            except ValueError as e:
                print(f'Erro ao converter a data de empréstimo, a data informada {dataEmprestimo} deve estar no formato dd/mm/aaaa. \n{e}')
        self.__dataEmprestimo = dataEmprestimo
    
    @property
    def dataDevolucao(self):
        return self.__dataDevolucao
    
    @dataDevolucao.setter
    def dataDevolucao(self, dataDevolucao):
        if dataDevolucao is None: 
            dataDevolucao = datetime.now()
        else:
            try:
                dataDevolucao = datetime.strptime(dataDevolucao, '%d/%m/%Y')
            except ValueError as e:
                print(f'Erro ao converter a data de devolução, a data informada {dataDevolucao} deve estar no formato dd/mm/aaaa. \n{e}')
        self.__dataDevolucao = dataDevolucao
  
    def registrarDevolucao(self, dataDevolucao = None):
        if self.status == 'Devolvido':
            print(f'Erro ao registrar Devolução! Este exemplar já foi devolvido')
        else:
            self.status = 'Devolvido'
            self.dataDevolucao = dataDevolucao
            self.exemplar.devolver()  
              
    def registrarRenovacao(self):
        if self.status == 'Emprestado':
            self.exemplar.renovar()
        else:
            print('Erro ao renovar empréstimo! Este exemplar já foi devolvido')
        
    def __str__(self):
        string = (f'\n=== Status Empréstimo ===\n'
                   f'Status: {self.status}\n'
                   f'Exemplar: {self.exemplar}\n'
                   f'Usuário: {self.usuario}\n'
                   f'Data de Empréstimo: {self.dataEmprestimo.strftime("%d/%m/%Y")}\n')
        if self.status == 'Devolvido':
            string += f'Data de Devolução: {self.dataDevolucao.strftime("%d/%m/%Y")}\n'
        else:
            string += 'Empréstimo ainda não devolvido'
        return string