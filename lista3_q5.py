'''5) Faça um programa que calcula a potência a partir
de dois valores digitados pelo usuário. Não use 
o operador de potência, faça apenas multiplicações.
Se o usuário digitar: base = 2, expoente = 3, o 
programa deve repetir a multiplicação 2 x 2 x 2 para
obter o resultado.'''

base = int(input("Base? "))
expo = int(input("Expoente? "))
mult = 1  # valor neutro da multiplicação

cont = 1 # valor inicial
while cont <= expo :   # teste lógico
    mult = mult * base
    cont = cont + 1   # incremento

print("Resultado = ", mult)





