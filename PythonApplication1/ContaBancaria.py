import textwrap

def menu():
    menu = """

 [d] Depositar
 [s] Sacar
 [nu] Novo Usuario
 [nv] Nova Conta
 [ls] Listar Contas
 [e] Extrato
 [q] Sair

=> """
    return input(textwrap.dedent(menu))
def Deposito(saldo, valor, extrato):
   valor = float(input("Informe o valor do dep�sito: "))

   if valor > 0:
     saldo += valor
     extrato += f"Dep�sito: R$ {valor:.2f}\n"

   else:
     print("Opera��o falhou! O valor informado � inv�lido.")
         
   return saldo, extrato   
def Saque(*, saldo, valor, extrato, limite_saque,limite, numero_saques):
     excedeu_saldo = valor > saldo

     excedeu_limite = valor > limite

     excedeu_saques = numero_saques >= limite_saque

     if excedeu_saldo:
       print("Opera��o falhou! Voc� n�o tem saldo suficiente.")

     elif excedeu_limite:
        print("Opera��o falhou! O valor do saque excede o limite.")

     elif excedeu_saques:
        print("Opera��o falhou! N�mero m�ximo de saques excedido.")

     elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

     else:
       print("Opera��o falhou! O valor informado � inv�lido.")
             
     return saldo, extrato
def Extrato(saldo, /, *, extrato):
   print("\n================ EXTRATO ================")
   print("N�o foram realizadas movimenta��es." if not extrato else extrato)
   print(f"\nSaldo: R$ {saldo:.2f}")
   print("==========================================")
def criar_usuario(usuarios):
   cpf = input("Informe seu CPF (somente numeros): ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("N�o foi possivel concluir a opera��o, o CPF informado j� est� cadastrado.")
      
   nome = input("Informe seu nome completo: ")
   data_nascimento = input("Informe sua data de nascimento: ")
   end = input("Informe seu endere�o (logradouro, nmr - bairro - cidade/estado): ")
   
   usuarios.append = ({"nome": nome, "data de nascimento": data_nascimento, "endereco": end})
def filtrar_usuario(cpf, usuario):
   usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuario_filtrado if usuario_filtrado else None
def criar_conta(agencia, numero_conta, usuario):
   cpf = input("Informe o CPF do usuario: ")
   usuario = filtrar_usuario(cpf, usuarios)
   
   if (usuario):
      print("Conta criada com sucesso!")
      return {"agencia": agencia, "numero da conta": numero_conta, "usuario": usuario}
   else:
      print("Usuario n�o encontrado.")
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
AGENCIA = 0001
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: R$"))
        saldo, extrato = Deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = Saque(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite_saque=LIMITE_SAQUES, 
            limite=limite, 
            numero_saques=numero_saques)
        
    elif opcao == 'nv':
       criar_usuario(usuarios)
       
    elif opcao == 'nu':
       numero_conta = len(contas) + 1
       conta = criar_conta(AGENCIA, numero_conta, usuarios)
       
       if conta:
          contas.append(conta)

    elif opcao == "e":
        Extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Opera��o inv�lida, por favor selecione novamente a opera��o desejada.")
 