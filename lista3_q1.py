'''1) Crie um programa que imprime a tabuada de um
número digitado pelo usuário. Ex. Usuário 
digitou "2", o programa imprime:
2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ... '''

tabuada = int(input("Tabuada de qual número? "))

num = 1   # valor inicial

while num <= 10 :   # teste lógico
    print(f"{tabuada} x {num} = {tabuada * num}")
    
    num = num + 1   # incremento

