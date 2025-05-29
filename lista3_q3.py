'''3) Crie um programa em que o usuário digite 10
números e o programa apresente a soma desses 
números. Dica: use uma variável para acumular a
soma dos números, como no exemplo:
soma = soma + numero.'''

cont = 1  # valor inicial
soma = 0

while cont <= 10 :  # teste lógico
    numero = int(input("Digite o número: "))
    soma = soma + numero
    
    cont = cont + 1 # incremento

print("A soma dos números é:", soma)
    