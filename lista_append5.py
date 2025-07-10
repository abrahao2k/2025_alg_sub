'''Escreva um programa que crie uma lista contendo números de
10 a 1 em ordem decrescente usando um loop "while". Em seguida,
exiba a lista resultante.'''

contagem = []
numero = 10
while numero > 0 :
    contagem.append(numero)
    numero -= 1

print(contagem)

