menu = """
Selecione a opção desejada:

[1] Consultar saldo
[2] Sacar
[3] Depositar
[4] Extrato
[5] Sair

"""
saldo = 0
limite = 500
saques = 0
extrato = ""
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print(f"Seu saldo atual é de: R$ {saldo}")

    elif opcao == 2:

        if saldo == 0:
            print(f"Saldo insuficiente. Seu saldo atual é de: R$ {saldo}")
            print("Retornando ao menu anterior...")

        elif saldo > 0 :
            valor = float(input("Informe o valor que deseja sacar: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Saldo insuficiente para sacar o valor desejado.")

            elif excedeu_limite:
                print("Valor do saque é superior ao limite permitido para a operação. Informe outro valor.")

            elif excedeu_saques:
                print("O limite de saques diário foi atingido. Tente outro dia.")

            elif valor > 0:
                saldo -= valor
                extrato = f"Saque: R$ {valor:.2f}\n"
                saques += 1
                print("Saque realizado com sucesso!")

    elif opcao == 3:
        valor = float(input("Informe o valor que deseja depositar: "))
        saldo += valor
        extrato = f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    
    elif opcao == 4:
        print("==========EXTRATO==========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

    elif opcao == 5:
        break

    else:
        print("Operação inválida. Por favor selecione uma opção válida.")