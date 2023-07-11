menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor do deposito "))
        if deposito > 0:
            saldo += deposito
            extrato += f"deposito: R$ {deposito:.2f}\n"
        else:
            print('operacao falhou! o valor informado e invalido.')
    elif opcao == "s":
        saque = float(input("digite o valor do saque "))
        if numero_saques == LIMITE_SAQUES:
            print("voce nao pode mais sacar")
        elif saldo != 0:
            if saque >= 500:
                print('voce passou do limite de R$ 500.00')
            elif saque > saldo:
                print('voce não tem saldo para isso')
            else:
                saldo -= saque
                numero_saques += 1
                extrato += (f'Saque: R$ {saque:.2f}\n')
        elif saque < 0:
            print('operacao falhou! o valor informado e invalido.')
        else:
            print("voce não tem saldo")

    elif opcao == "e":
        print("\n ================ Extrato ===================")
        print("\n Não foram realizados movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n ============================================")

    elif opcao == "q":
        break
    
    else:
        print("operacao invalida, por favor selecionar novamente a operacao desejada.")