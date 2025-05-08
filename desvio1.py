# Digitar a temperatura do ar condicionado
# E dizer "Está Calor" se for acima de 25 graus

temp = int(input("Digite a temperatura: "))

if temp > 25 :
    print("Que calor!")
    print("Esfrie mais!")

if temp >= 18 :
    if temp <= 25:
        print("Temperatura agradável.")

if temp < 18 :
    print("Que frio!")
    print("Esquente mais!")

print("Terminou.")

