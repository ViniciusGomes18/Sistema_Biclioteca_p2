import pickle
from ListaEncadeada import ListaEncadeada
from Livro import Livro
from Emprestimo import Emprestimo
from Leitor import Leitor
from carteirinha import Gerar_Carteirinha

class Biblioteca:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.livros = {} #Armazena Estoque de Livros em Dict e Suas informações dentro de tuplas
        self.leitores = {} # Armazena Leitores em Dict e Suas informações dentro de tuplas
        self.emprestimos = []
        self.fila_reservas = {}
        self.devolucoes_recentes = []
        self.leitores_por_livro = {}
        self.historico = ListaEncadeada()

    def Cadastrar_Livro(self):
        novo_livro = Livro()
        titulo = novo_livro.dados[0]

        if titulo in self.livros:
            print(f"O livro '{titulo}' já está cadastrado")
        else:
            self.livros[titulo] = novo_livro.dados
            print(f"O livro '{titulo}' foi cadastrado com sucesso")
            self.Salvar_Dados()

    def Excluir_Livro(self, livro):
        if livro in self.livros:
            self.livros.pop(livro)
            print(f'O livro "{livro}" foi excluído com sucesso do estoque')
            self.Salvar_Dados()
        else:
            print(f'O livro "{livro}" não existe no estoque')

    # Leitores: Cadastro
    def Cadastrar_Leitor(self):
        novo_leitor = Leitor()
        cpf = novo_leitor.dados[1]
        if cpf in self.leitores:
            print(f"O leitor {novo_leitor.dados[0]} já está cadastrado")
        else:
            self.leitores[cpf] = novo_leitor.dados
            print(f"O leitor {novo_leitor.dados[0]} foi cadastrado com sucesso")
            self.Salvar_Dados()

    def Excluir_Leitor(self, cpf):
        if cpf in self.leitores:
            nome = self.leitores[cpf][0]
            self.leitores.pop(cpf)
            print(f"O leitor {nome} foi excluído com sucesso.")
            self.Salvar_Dados()
        else:
            print(f"O leitor com CPF {cpf} não existe no cadastro.")


    def Emprestar_Livro(self, titulo, cpf):
        if titulo in self.livros and self.livros[titulo][4][0] > 0: #verifica se o titulo existe e se o livro está disponível
            self.livros[titulo][4][0] -= 1

            emprestimo = Emprestimo(
                id_emprestimo=len(self.emprestimos) + 1,
                leitor=self.leitores[cpf],
                livros=[titulo]
            )

            self.emprestimos.append(emprestimo)

            if titulo not in self.leitores_por_livro:
                self.leitores_por_livro[titulo] = set()
            self.leitores_por_livro[titulo].add(cpf)

            self.Salvar_Dados()
            print(f"O livro '{titulo}' foi emprestado para {self.leitores[cpf][0]} com sucesso em {emprestimo.data_emprestimo}!")
        else:
            print(f"O livro '{titulo}' não está disponível para empréstimo.")

    def Devolver_Livro(self, livro, leitor):
        if livro in self.livros:
            self.livros[livro][4][0] += 1
            self.Salvar_Dados()
            print(f'O livro {livro} foi devolvido com sucesso!')


    def Livros_Mais_Populares_Unicos(self):
        if not self.leitores_por_livro:
            print("Nenhum empréstimo foi registrado ainda.")
            return

        mais_popular = max(self.leitores_por_livro.items(), key=lambda item: len(item[1]))
        titulo, leitores_set = mais_popular
        print(f"O livro mais popular é '{titulo}' com {len(leitores_set)} leitores únicos.")

    def Gerar_Carteirinha_Leitor(self, cpf):
        if cpf not in self.leitores:
            print("Leitor não encontrado.")
            return

        leitor = self.leitores[cpf]
        Gerar_Carteirinha(leitor, cpf, self.emprestimos)

    def Atualizar_Contato(self, cpf):
        if cpf not in self.leitores:
            print("Leitor não encontrado.")
            return

        leitor = self.leitores[cpf]
        while True:
            print("\n1. Alterar Email")
            print("2. Alterar Telefone")
            print("3. Voltar")
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    novo_email = input("Digite o novo email: ").strip()
                    self.email = novo_email
                    print("Email alterado com sucesso!")
                elif escolha == 2:
                    novo_telefone = input("Digite o novo telefone: ").strip()
                    self.telefone = novo_telefone
                    print("Telefone alterado com sucesso!")
                elif escolha == 3:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Apenas números inteiros são aceitos.")
            
    

    def Listar_Leitores(self):
        if not self.leitores:
            print("Nenhum leitor cadastrado.")
            return
        print("\n=== Leitores Cadastrados ===")
        for cpf, dados in self.leitores.items():
            print(f"Nome: {dados[0]} | CPF: {cpf}")
def Salvar_Dados(self):
        with open("biblioteca.pkl", "wb") as f:
            pickle.dump(self, f)