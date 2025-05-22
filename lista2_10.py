'''10) Escreva um programa que o usuário informa
o valor do salário e o programa calcula o novo
salário de acordo com as seguintes condições: 
Até R$ 1000,00 - aumento 15%
Até R$ 2000,00 - aumento 10%
Até R$ 3000,00 - aumento 5%
Acima de R$ 3000,00 - aumento 2.5%
novo = salario + (salario * 15 / 100)
'''
salario = float(input("Salário atual: ").replace(',' , '.'))
if salario <= 1000 :
    print("Novo = R$", salario+(salario*15/100))
elif salario <= 2000 :
    print("Novo = R$", salario+(salario*10/100))
elif salario <= 3000 :
    print("Novo = R$", salario+(salario*5/100))
else:
    print("Novo = R$", salario+(salario*2.5/100))