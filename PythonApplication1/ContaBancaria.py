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
     deposito = float(input("Informe o valor que deseja depositar: R$"))
     saldo += deposito
     
 elif operacao_desejada == "s" :
    if numero_saques < LIMITE_SAQUE:
       saque = float(input("Informe o valor que deseja sacar: R$"))
       
       if saldo >= saque :
        saldo -= saque
        valor_saque += saldo
        numero_saques += 1
       elif saque > saldo :
          print("Valor de saque maior que saldo disponivel!")
          break
       else :
          print("Limite diario de saques atingido!")
          break
 elif operacao_desejada == "e" :
     exc = "Extrato"
     extrato = f'''
Saldo disponivel: R${saldo}  
Numero de saques realizados: {numero_saques}
      '''
     print(exc.center(19, "#"))
     print(extrato)
     
     break
    
 elif operacao_desejada == "sr" :
    print("Volte sempre")
    break
 
 else :
   print("Operacao invalida")

