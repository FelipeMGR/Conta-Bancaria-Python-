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
while True :
 operacao_desejada = input('''Selecione a operação desejada: 
                                Deposito (D)
                                Extrato (E)
                                Saque (S)
                                Sair (SR)
                                ''').lower()
 if  operacao_desejada == "D" :
     deposito = float(input("Informe o valor que deseja depositar: R$"))
     saldo += deposito
     
 elif operacao_desejada == "S" :
    if numero_saques < LIMITE_SAQUE:
       saque = float(input("Informe o valor que deseja sacar: R$"))
       
       if saldo >= saque :
        saldo -= saque
        valor_saque += saldo
        numero_saques += 1
       else :
    else :
       print("Ocorreu um erro ao realizar seu saque. Verifique se o valor de saque está dentro de seu orçamento, e se ainda está dentro do limite de saque diário.")
 elif operacao_desejada == "E" :
    
    print(f"Valor total dos saques: R${valor_saque}")
    print(f"Seu saldo atual é de: R${saldo}")
    print(f"Quantidade de saques realizados: {numero_saques}")
    
 elif operacao_desejada == "SR" :
    print("Volte sempre!")
    break
 
 else :
   print("Operação inválida.")

