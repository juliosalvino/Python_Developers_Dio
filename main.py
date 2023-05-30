menu = """
Escolha sua opção:

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

saldo = 0
limite_por_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:

    print(menu)
    opcao = input("Digite a opção desejada: ")

    if opcao == "d":
        deposito = float(input("Digite o valor a ser depositado: "))
        saldo += deposito
        valor_depositado = "Depósito de R$ "+ str(deposito)
        extrato.append(valor_depositado)
        print(f"O seu saldo atual é de R$ {saldo}")
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Dgite o valor a ser sacado: "))
            if saque <= saldo:
                if saque > limite_por_saque:
                    print(f"Valor não permitido, o valor máximo permitido é de {limite_por_saque}")
                else:
                    print(f"Sacando o valor de R$ {saque} ...")
                    saldo -= saque
                    numero_saques += 1
                    valorsacado = "Saque de - R$ "+ str(saque)
                    extrato.append(valorsacado)
                    print(f"O seu saldo atual é de R$ {saldo}")
            else:
                print("Saldo insuficiente!")
        else:
            print(f"O limite de saques diários foi excedido, o limite máximo permitido é de {LIMITE_SAQUES}")

    elif opcao == "e":
        for item in extrato:
            print(item)
        print("")
        print(f"O seu saldo disponível é de R$ {saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione a opção desejada.")