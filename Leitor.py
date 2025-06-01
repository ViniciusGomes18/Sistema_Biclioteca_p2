from datetime import datetime

class Leitor:
    def __init__(self):
        nome = input("Digite o nome: ")

        # Formatação do CPF
        while True:
            cpf = input("Digite o CPF (somente números): ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print("CPF inválido. Digite exatamente 11 números.")

        # Formatação da data de nascimento
        while True:
            try:
                data = input("Digite a data de nascimento (DD/MM/AAAA): ")
                data_nasc = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")

        # Verificação do e-mail
        while True:
            email = input("Digite o email: ")
            if "@" in email and "." in email:
                break
            else:
                print("Email inválido.")

        # Formatação do telefone
        while True:
            tel = input("Digite o telefone (somente números): ")
            if tel.isdigit() and len(tel) == 11:
                telefone = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
                break
            else:
                print("Telefone inválido. Digite exatamente 11 números.")

        # Criando a tupla com lista para dados mutáveis
        self.dados = (
            nome,            # 0
            cpf,             # 1
            data_nasc,       # 2
            [email, telefone]  # 3 -> lista mutável
        )

    def __str__(self):
        return (
            f"Nome: {self.dados[0]} | CPF: {self.dados[1]} | "
            f"Nascimento: {self.dados[2]} | Email: {self.dados[3][0]} | Telefone: {self.dados[3][1]}"
        )