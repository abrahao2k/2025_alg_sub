# OPERADOR LÓGICO AND (TODAS VERDADEIRAS)

usuario = input("Usuário? ")
senha = input("Senha? ")

if usuario == "adm" and senha == "9876" :
    print("Acesso permitido.")
else:
    print("Acesso negado.")


'''
if usuario == "adm" :
    if senha == "9876" :
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
else:
    print("Acesso negado.")
'''