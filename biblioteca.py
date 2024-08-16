from livros import Livro
from usuario import Usuario
from exemplar import Exemplar
from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuario = []
        self.__emprestimos = []

    def adicionar_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)
            print(f"O livro {livro.titulo} - Editora {livro.editora} foi adicionado com sucesso!\n")
        else:
            print(f"Não foi possível adicionar o livro. O objeto fornecido deve ser uma instância da classe Livro. Recebido: {type(livro)}")

    def registrar_usuario(self, usuraio: Usuario):
        if isinstance(usuraio, Usuario):
            self.__usuario.append(usuraio)
            print("Usuário registrado com sucesso!\nDetalhes do usuário:")
            print(f"Nome: {usuraio.nome}\nTelefone: {usuraio.telefone}\nNacionalidade: {usuraio.nacionalidade}\n")
        else:
            print(f"Não foi possível registrar o usuário. O objeto fornecido deve ser uma instância da classe Usuario. Recebido: {type(usuraio)}")
    
    def emprestar_livro(self, exemplar: Exemplar, usuario: Usuario):
        if isinstance(exemplar, Exemplar) and isinstance(usuario, Usuario):
            for livro in self.__livros:
                if exemplar in livro.lista_exemplares:
                    emprestimo = Emprestimo(usuario, exemplar)
                    self.__emprestimos.append(emprestimo)
                    break
        else:
            print(f"Não foi possível realizar o empréstimo. O exemplar e o usuário devem ser instâncias das classes Exemplar e Usuario, respectivamente. Recebido: {type(exemplar)} e {type(usuario)}")
          
    def devolver_livro(self, exemplar: Exemplar):
        if isinstance(exemplar, Exemplar):
            for emprestimo in self.__emprestimos:
                if emprestimo.exemplar == exemplar and emprestimo.status == 'Emprestado':
                    emprestimo.registrarDevolucao()
                    print(f"O exemplar {exemplar.id} do livro '{exemplar.titulo}' foi devolvido com sucesso.")
                    return
            print(f"Não foi encontrado um empréstimo ativo para o exemplar {exemplar.id}.")
        else:
            print(f"Não foi possível devolver o exemplar. O objeto fornecido deve ser uma instância da classe Exemplar. Recebido: {type(exemplar)}")

    def renovar_livro(self, exemplar: Exemplar, usuario: Usuario):
        if isinstance(exemplar, Exemplar) and isinstance(usuario, Usuario):
            for emprestimo in self.__emprestimos:
                if emprestimo.exemplar == exemplar and emprestimo.usuario == usuario and emprestimo.status == 'Emprestado':
                    emprestimo.registrarRenovacao()
                    print(f"O empréstimo do exemplar {exemplar.id} do livro '{exemplar.titulo}' foi renovado com sucesso para {usuario.nome}.")
                    return
            print(f"Não foi encontrado um empréstimo ativo do exemplar {exemplar.id} para o usuário {usuario.nome}.")
        else:
            print(f"Não foi possível renovar o empréstimo. O exemplar e o usuário devem ser instâncias das classes Exemplar e Usuario, respectivamente. Recebido: {type(exemplar)} e {type(usuario)}")   

livro1 = Livro(
    titulo="A Vida Secreta das Árvores",
    editora="Editora X",
    generos=["Natureza", "Ciência"],
    autores=["Peter Wohlleben"],
)

usuario1 = Usuario(
    nome="Maria Silva",
    telefone="999990000",
    nacionalidade="brasileira"
)

exemplar1 = Exemplar(
    1, 
    titulo="A Vida Secreta das Árvores",
    editora="Editora X",
    generos=["Natureza", "Ciência"],
    autores=["Peter Wohlleben"]
)

exemplar2 = Exemplar(
    2,
    titulo="A Vida Secreta das Árvores",
    editora="Editora X",
    generos=["Natureza", "Ciência"],
    autores=["Peter Wohlleben"]
)

livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.registrar_usuario(usuario1)

biblioteca.emprestar_livro(exemplar1, usuario1)
biblioteca.renovar_livro(exemplar1, usuario1)
biblioteca.devolver_livro(exemplar1)


