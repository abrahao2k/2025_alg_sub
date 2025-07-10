'''Peça ao usuário para inserir nomes em uma lista usando
um loop "while". Continue pedindo nomes até que o usuário
insira a palavra "fim". Em seguida, exiba a lista de nomes.'''

lista = []
nome = "a"

while nome != "fim" :
    nome = input("Digite um nome: ")
    lista.append(nome)

## fora do laço ##
lista.pop()   # remove o último item ("fim")
print(lista)

