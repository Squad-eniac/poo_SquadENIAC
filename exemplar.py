class Exemplar:
    def __init__(self, id):
        self.id = id
        self.disponivel = True
        self.numAtualRenovacoes = 0

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Exemplar {self.id} - empréstimo feito com sucesso")
        else:
            print(f"Exemplar {self.id} - não está disponível para empréstimo")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Exemplar {self.id} - devolvido com sucesso")
        else:
            print(f"Exemplar {self.id} - não está com empréstimo ativo")
    
    def renovar(self):
        self.numAtualRenovacoes += 1
        print(f"Exemplar {self.id} foi renovado. Renovação atual: {self.numAtualRenovacoes}.")