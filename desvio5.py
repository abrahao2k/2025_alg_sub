'''Escreva um programa que pergunta qual a melhor
escola de Mossoró. Se o usuário responder IFRN,
diga que acertou, se for outra escola,
diga que errou.'''

escola = input("Qual é a melhor escola de Mossoró? ")

if escola.upper() == "IFRN" :   #transforma em maiúsculas
    print("Você acertou! :) ")
else:
    print("Você errou! :( ")

