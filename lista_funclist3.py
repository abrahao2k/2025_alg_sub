'''3 - Crie uma lista com números repetidos e peça ao usuário
para inserir um número. Use um loop while para remover todas
as ocorrências desse número da lista.'''

lista = [1, 2, 3, 1, 5, 9, 8, 4, 6, 1, 2, 3, 5, 7, 8, 6, 9, 1]
print(lista)

num = int(input("Digite um número para remover: "))

while num in lista:
    lista.remove(num)

print(lista)