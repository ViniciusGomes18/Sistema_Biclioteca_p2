import pickle
import os

def Carregar_Biblioteca():
    if os.path.exists("biblioteca.pkl"):
        with open("biblioteca.pkl", "rb") as f:
            return pickle.load(f)
    else:
        return Biblioteca("Biblioteca Central", "Rua das Letras, 123")

def Exibir_Menu():
    print("\n" + "=" * 45)
    print("☺  SISTEMA DE BIBLIOTECA  ☺".center(45))
    print("=" * 45)
    print("1. Cadastrar Livro")
    print("2. Cadastrar Leitor")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Ver Livro Mais Popular (leitores únicos)")
    print("6. Carteirinha do Leitor")
    print("7. Área do Bibliotecario")
    print("8. Sair")
    print("=" * 45)

def area_bibliotecario(biblioteca):
    senha = input("\nDigite a senha de acesso: ")
    if senha != "admin123":
        print("Senha incorreta! Acesso negado.")
        return

    while True:
        print("\n--- Área do Bibliotecário ---")
        print("1. Excluir Livro")
        print("2. Editar Contato do Leitor")
        print("3. Excluir Leitor")
        print("4. Listar Leitores Cadastrados")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            titulo = input("Digite o título do livro a ser excluído: ").strip()
            biblioteca.Excluir_Livro(titulo)

        elif escolha == "2":
            cpf = input("Digite o CPF do leitor: ").strip()
            biblioteca.Atualizar_Contato(cpf)
        elif escolha == "3":
            cpf = input("Digite o CPF do leitor: ").strip()
            biblioteca.Excluir_Leitor(cpf)

        elif escolha == "4":
            biblioteca.Listar_Leitores()

        elif escolha == "5":
            break
        else:
            print("Opção inválida.")

def Main():
    biblioteca = Carregar_Biblioteca()

    while True:
        Exibir_Menu()
        try:
            opcao = int(input("Escolha uma opção: ").strip())
            
            if opcao == 1:
                print("\nCadastro de Livro")
                biblioteca.Cadastrar_Livro()

            elif opcao == 2:
                print("\nCadastro de Leitor")
                biblioteca.Cadastrar_Leitor()

            elif opcao == 3:
                print("\nEmpréstimo de Livro")
                titulo = input("Título do livro: ").strip()
                cpf = input("CPF do leitor: ").strip()
                biblioteca.Emprestar_Livro(titulo, cpf)

            elif opcao == 4:
                print("\nDevolução de Livro")
                titulo = input("Título do livro a devolver: ").strip()
                cpf = input("CPF do leitor: ").strip()
                biblioteca.Devolver_Livro(titulo, cpf)

            elif opcao == 5:
                print("\nLivro mais popular por leitores únicos:")
                biblioteca.Livros_Mais_Populares_Unicos()

            elif opcao == 6:
                print("\nCarteirinha do Leitor")
                cpf = input("Digite o CPF do leitor: ").strip()
                biblioteca.Gerar_Carteirinha_Leitor(cpf)
            
            elif opcao == 7:
                area_bibliotecario(biblioteca)

            elif opcao == 8:
                print("\nAté logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")

# Executa o programa
Main()


def listar_leitores():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            leitores = arquivo.readlines()
            if not leitores:
                print("Nenhum leitor cadastrado ainda.")
                return
            print("\n===== Leitores Cadastrados =====")
            for leitor in leitores:
                print(leitor.strip())
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
