menu = """

[S] - Sacar
[E] - Extrato
[D] - Depositar

[Q] - QUIT

Digite a opção:"""
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500
saldo = 0 
extrato = ""
numero_saques=0


while True:
    opcao = input(menu)

    if opcao.upper() == "D":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou. O valor informado é inválido")

    elif opcao.upper() == "S":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_POR_SAQUE

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if  excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif  excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif  excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        
        elif  valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques+=1

        else:
            print("Operação falhou. Valor inválido")

            
    elif opcao.upper() == "E":
        print("\n", "="*10, "EXTRATO", "="*10)
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("="*30)

    elif opcao.upper() == "Q":
        break

    else:
        print("Opção Inválida. Tente novamente.")
        
