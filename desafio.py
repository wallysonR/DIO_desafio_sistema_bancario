MENU = '''
Qual operação deseja realizar ? 
[1] - Deposito 
[2] - Saque
[3] - Extrato
'''
limite_saque=3
saldo=0.0
extrato = []
while True:
    opcao = int(input(MENU))
    if(opcao == 1):
        valor_deposito = float(input("Qual valor que deseja depositar ?"))
        if(valor_deposito>0):
            saldo += valor_deposito
            extrato.append(f'Voce depositou {valor_deposito}')
            print(f'Valor depositado com sucesso, seu saldo é de {saldo}')
            continue
        else:
            print("Valor incorreto.")
    elif(opcao == 2):
        if(saldo>0.0):
            if(limite_saque>0):
                valor_saque = float(input("Quando deseja sacar ?"))
                if(valor_saque<saldo):
                    saldo -= valor_saque
                    limite_saque -= 1
                    extrato.append(f'Voce sacou {valor_saque}')
                    print(f'Valor sacado com sucesso, seu saldo é de {saldo}')
                    continue
                else:
                    print('Seu saldo é insulficiente');
            else:
                print("Limite de saque atingido")
    elif(opcao == 3):
        variavel_temporaria = "EXTRATO"
        print("EXTRATO".center(20,"#"))
        for atividade in extrato:
            print(atividade)
        print(f'Seu saldo é de R${saldo}')
        continue
    else:
        break

