from autores import Autores

class Livro:
    def __init__(self, titulo, editora, generos, autores=None, max_renovacoes=3):
        self.__titulo = titulo
        self.__editora = editora
        self.__generos = generos
        self.__autores = autores if autores else[]  
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
        self.__lista_exemplares.append(exemplar)
        print(f"Exemplar {exemplar.id} adicionado ao livro '{self.__titulo}'")

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


# Teste

autor1 = Autores(nome="Laysa Alexia")
autor2 = Autores(nome="Lima Cipriano")

livro1 = Livro(titulo="Python para Iniciantes", editora="Editora XYZ", generos=["Tecnologia", "Programação"], autores=[autor1])
livro2 = Livro(titulo="Avançando com Python", editora="Editora ABC", generos=["Tecnologia", "Programação"])

autor1.adicionar_livro(livro1)
autor2.adicionar_livro(livro2)
autor1.adicionar_livro(livro2)

print(autor1)  # Esperado: "Laysa Alexia"
print(autor2)  # Esperado: "Lima Cipriano"
print(livro1)  # Esperado: "'Python para Iniciantes' de Laysa Alexia, Editora: Editora XYZ, Gêneros: Tecnologia, Programação, Exemplares: 0"
print(livro2)  # Esperado: "'Avançando com Python' de Laysa Alexia, Lima Cipriano, Editora: Editora ABC, Gêneros: Tecnologia, Programação, Exemplares: 0"
