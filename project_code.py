menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Selecione uma opção """

limite = 500
extrato = ""
saldo = 0
saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido")

    elif opcao == 2:
        valor = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insifuciente. Informe outro valor.")
        
        elif excedeu_limite:
            print("Falha! O valor do saque é superior ao limite de R$ 500")

        elif excedeu_saques:
            print("Falha! Limite de saque diário atingido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1

        else:
         print("Falha. Tente novamente")

    elif opcao == 3:
        print("Extrato")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------")

    elif opcao == 4:
        break

    else:
        print("Erro intero. Tente novamente")
    