def Gerar_Carteirinha(leitor, cpf, emprestimos):
    nome = leitor[0]
    email = leitor[3][0]
    nascimento = leitor[2]

    emprestimos_do_leitor = [e for e in emprestimos if e.leitor[1] == cpf]

    total = len(emprestimos_do_leitor)
    ultimo_emprestimo = emprestimos_do_leitor[-1].livros[0] if total > 0 else "Nenhum"

    carteirinha = f"""
--------------------------------------
      ☻ CARTEIRINHA DO LEITOR ☻
--------------------------------------
 Nome: {nome}
 CPF: {cpf}
 Email: {email}
 Nascimento: {nascimento}
 Último livro emprestado: {ultimo_emprestimo}
 Total de empréstimos: {total}
--------------------------------------
"""
    print(carteirinha)