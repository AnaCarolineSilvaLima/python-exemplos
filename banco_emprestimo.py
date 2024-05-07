print(f"Programa de emprestimo\n"
      f"Responda: (0-Não ou 1-Sim)")
nome_negativado=int(input("Possui nome negativado?: "))
if nome_negativado == 1:
    print("Não pode realializar o empréstimo")
else:
    carteira_assinada=int(input("Possui carteitra assinada?: "))
    if carteira_assinada == 0:
        print("Não pode realizar empréstimo")
    else:
        casa_propria=int(input("Possui casa própria?: "))
        if casa_propria == 0:
            print("Não pode realizar o epréstimo")
        else:
            print("Conceder empréstimo")