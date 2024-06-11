#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

# Deve ser possivel depositar valores positivos, trabalha apenas com 1 usuario,não precisa preocupar com num. de agencia e CC, todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato.

# O sistema deve permitir realizar 3 saques diários com limite máximo de 500,00 por saque, se não tiver saldo sufic. apresentar mensagem de não tem saldo sufic. todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.

# Essa operação deve listar todos os depositos e saques realizados na conta, no fim da lostagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = $ 1500.45

menu ="""

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIM_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIM_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excedeu o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido")
            


    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("===========================")
        
        

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")