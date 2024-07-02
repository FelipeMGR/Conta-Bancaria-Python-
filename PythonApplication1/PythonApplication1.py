menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
saque = 0
deposito = 0
numero_saques = 0
extrato = ""
LIMITE_SAQUE = 3
valor_saque = 0
operacao_desejada = ""

while True :
 operacao_desejada = input('''Selecione a operacao desejada: 
                                Deposito (D)
                                Extrato (E)
                                Saque (S)
                                Sair (SR)
                                ''').lower()
 if  operacao_desejada == "d" :
     deposito = float(input("Informe o valor que deseja depositar: "))
     saldo += deposito
     
 elif operacao_desejada == "s" :
    if numero_saques < LIMITE_SAQUE:
       saque = float(input("Informe o valor que deseja sacar: "))
       
       if saldo >= saque :
        saldo -= saque
        valor_saque += saldo
        numero_saques += 1
       else :
        print("Ocorreu um erro ao realizar seu saque. Verifique se o valor de saque esta dentro de seu orcamento, e se ainda esta dentro do limite de saque diario")
 elif operacao_desejada == "e" :
    
    print(f"Valor total dos saques: {valor_saque}")
    print(f"Seu saldo atual e de: {saldo}")
    print(f"Quantidade de saques realizados: {numero_saques}")
    break
    
 elif operacao_desejada == "sr" :
    print("Volte sempre")
    break
 
 else :
   print("Operacao invalida")

