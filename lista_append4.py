'''Crie um programa que preencha uma lista com números pares
automaticamente usando um loop "while". A lista deve conter
os primeiros 10 números pares.
'''

numeros = []   #lista vazia

n = 2
while n <= 20 :
    numeros.append(n)
    n += 2

## fora do laço ##
print(numeros)

