'''11) Faça um programa que leia a idade de um
atleta e informa a qual categoria ele pertence: 
Até 8 anos - pré-mirim
Até 11 anos - mirim
Até 14 anos - infantil
Até 17 anos - juvenil
18 ou mais - adulto
'''
idade = int(input("Idade do atleta: "))

if   idade <= 8  : print("Pré-Mirim")
elif idade <= 11 : print("Mirim")
elif idade <= 14 : print("Infantil")
elif idade <= 17 : print("Juvenil")
else:              print("Adulto")