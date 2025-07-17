# crie uma função que pergunta o nome do usuário e adiciona
# o nome em uma lista

lista = list()  # cria uma lista vazia

def cadastrar():
    print("=== CADASTRO DE CLIENTE ===")
    nome = input("Nome do clinte: ")
    lista.append(nome)
    print("Cadastrado com sucesso.\n")

def imprimir():
    print("=== RELATÓRIO DE CLIENTES ===")
    for nome in lista:
        print(nome)
    print("--------------------")
    print(len(lista), "clientes cadastrados.")
    

##########################################################
# INÍCIO DO PROGRAMA
##########################################################
while True :
    op=int(input("MENU\n 1-Cadastrar\n 2-Imprimir\n 3-Sair\n Opção? "))
    if   op == 1 : cadastrar()
    elif op == 2 : imprimir()
    else : break