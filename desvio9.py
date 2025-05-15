# OPERADOR LÓGICO OR (QUALQUER VERDADEIRA)

# Os treinos de futebol acontecem segunda, quarta e sexta.
# Pergunte o dia da semana e diga se tem treino hoje.

dia = input("Que dia da semana é hoje? ")

if dia == "segunda" or dia == "quarta" or dia == "sexta":
    print("HOJE TEM TREINO! :) ")
else:
    print("NÃO TEM TREINO. :( ")

