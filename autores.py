from pessoa import Pessoa

class Autores(Pessoa):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.livros = []
        
    
    def adicionar_livro(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
            if self not in livro.autores:
                livro.autores.append(self)
                
    def __str__(self):
        return self.nome
    
