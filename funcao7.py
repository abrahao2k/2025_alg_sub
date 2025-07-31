# FUNÇÃO COM RETORNO
# passe 2 valores e retorne o MAIOR.
# se forem iguais, retorna qualquer um deles
def maior(v1, v2):
    if   v1 == v2 : return v1
    elif v1 > v2  : return v1
    else          : return v2

################################################
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
print("Maior valor:", maior(a,b) )
