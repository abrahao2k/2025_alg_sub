# ESCONDER A SENHA DIGITADA
import getpass

# AND E OR NO MESMO IF

usu = input("Usuário: ")
sen = getpass.getpass("Senha: ")  # não mostra o que é digitado

if (usu=="adm" and sen=="9876") or (usu=="gerente" and sen=="4567"):
    print("Acesso permitido.")

else:
    print("Acesso negado.")