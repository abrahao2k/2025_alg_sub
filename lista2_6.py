'''Escreva um programa que calcule o preço a pagar pelo
fornecimento de energia elétrica. Pergunte a
quantidade de kWh consumidas e o tipo de instalação:
R para residências, I para indústrias e C para comércios. 
Calcule o preço a pagar de acordo com a tabela a seguir'''

consumo = float(input("Consumo? "))
tipo = input("Tipo da instalação (R/I/C)? ")

if tipo.upper() == "R" :   # upper - converte para MAIUSCULA
    if consumo <= 500 : print("Tarifa = R$", consumo * 0.40)
    else: print("Tarifa = R$", consumo * 0.65)

elif tipo.upper() == "C" :
    if consumo<=1000: print("Tarifa = R$", consumo * 0.55)
    else: print("Tarifa = R$", consumo * 0.60)

elif tipo.upper() == "I" :
    if consumo<=5000: print("Tarifa = R$", consumo * 0.55)
    else: print("Tarifa = R$", consumo * 0.60)

else:
    print("Tipo de instalação inválida.")
    
    