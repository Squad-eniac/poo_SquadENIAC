from exemplar import Exemplar

class Livro:
    def __init__(self, titulo, editora, generos, autores, max_renovacoes=3):
        self.__titulo = titulo
        self.__editora = editora
        self.__generos = generos
        self.__autores = autores  
        self.__lista_exemplares = []  
        self.__max_renovacoes = max_renovacoes

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def generos(self):
        return self.__generos

    @generos.setter
    def generos(self, generos):
        self.__generos = generos

    @property
    def autores(self):
        return self.__autores

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @property
    def lista_exemplares(self):
        return self.__lista_exemplares

    @property
    def max_renovacoes(self):
        return self.__max_renovacoes

    @max_renovacoes.setter
    def max_renovacoes(self, max_renovacoes):
        self.__max_renovacoes = max_renovacoes

    def adicionar_exemplar(self, exemplar):
        """Adiciona um exemplar do livro à lista de exemplares"""
        if isinstance(exemplar, Exemplar):
            self.__lista_exemplares.append(exemplar)
            print(f"Exemplar {exemplar.id} adicionado ao livro '{self.__titulo}'")
        else:
            print("Erro: O objeto fornecido não é uma instância da classe Exemplar.")

    def remover_exemplar(self, exemplar):
        """Remove um exemplar do livro da lista de exemplares"""
        if exemplar in self.__lista_exemplares:
            self.__lista_exemplares.remove(exemplar)
            print(f"Exemplar {exemplar.id} removido do livro '{self.__titulo}'")
        else:
            print("Erro: Exemplar não encontrado na lista.")

    def __str__(self):
        autores_nomes = ', '.join([autor.nome for autor in self.__autores])
        generos_nomes = ', '.join(self.__generos)
        return f"'{self.__titulo}' de {autores_nomes}, Editora: {self.__editora}, Gêneros: {generos_nomes}, Exemplares: {len(self.__lista_exemplares)}"


