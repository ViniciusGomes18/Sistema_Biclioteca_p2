from No import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, acao):
        novo = No(acao, self.inicio)
        self.inicio = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.acao)
            atual = atual.proximo