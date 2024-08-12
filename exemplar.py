class Exemplar:
    def __init__(self, id):
        self.__id = id
        self.__disponivel = True
        self.__numAtualRenovacoes = 0

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Exemplar {self.__id} - empréstimo feito com sucesso")
        else:
            print(f"Exemplar {self.__id} - não está disponível para empréstimo")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Exemplar {self.__id} - devolvido com sucesso")
        else:
            print(f"Exemplar {self.__id} - não está com empréstimo ativo")
    
    def renovar(self):
        self.__numAtualRenovacoes += 1
        print(f"Exemplar {self.__id} foi renovado. Renovação atual: {self.__numAtualRenovacoes}.")
