from livros import Livro

class Exemplar(Livro):
    def __init__(self, id, titulo, editora, generos, autores, max_renovacoes=3):
        super().__init__(titulo, editora, generos, autores, max_renovacoes)
        self.__id = id
        self.__disponivel = True
        self.__numAtualRenovacoes = 0

    @property
    def id(self):
        return self.__id

    def emprestar(self):
        """Marca o exemplar como emprestado se estiver disponível."""
        if self.__disponivel:
            self.__disponivel = False
            print(f"Exemplar {self.__id} - empréstimo feito com sucesso")
        else:
            print(f"Exemplar {self.__id} - não está disponível para empréstimo")

    def devolver(self):
        """Marca o exemplar como devolvido se estiver emprestado."""
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Exemplar {self.__id} - devolvido com sucesso")
        else:
            print(f"Exemplar {self.__id} - não está com empréstimo ativo")
    
    def renovar(self):
        """Renova o empréstimo do exemplar se o limite de renovações não tiver sido atingido."""
        if self.__numAtualRenovacoes < self.max_renovacoes:
            self.__numAtualRenovacoes += 1
            print(f"Exemplar {self.__id} foi renovado. Renovação atual: {self.__numAtualRenovacoes}.")
        else:
            print(f"Exemplar {self.__id} atingiu o limite máximo de renovações.")
    
    def __str__(self):
        """Retorna uma representação em string do exemplar e das informações do livro associado."""
        return f"Exemplar ID: {self.__id} | Livro: {super().__str__()} | Disponível: {self.__disponivel}"

