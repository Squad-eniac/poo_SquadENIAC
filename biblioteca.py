from livros import Livro
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuario = []

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


biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.registrar_usuario(usuario1)
