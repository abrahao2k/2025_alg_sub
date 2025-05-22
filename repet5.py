# REPETIÇÃO COM CONDIÇÃO MÚLTIPLA - AND
# faça um programa que aceita a digitação de várias notas entre 0 e 100
# se digitar uma nova inválida, o programa finaliza

nota = 0   # valor inicial, pode ser qualquer número entre 0 e 100

while nota >= 0 and nota <= 100 :  # teste lógico, 2 condições
    
    nota = int(input("Digite a nota: "))  # incremento (mudança)

#else:                   # opcional
print("Nota inválida.")