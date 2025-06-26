# UM LAÇO PARA CADASTRAR VÁRIOS ITENS
lista = []  # lista vazia

while True:    # laço infinito
    item = input("Digite o item: ")
    lista.append(item) # acrescentar na lista
    # lista.append(input("Digite o item: "))
    
    resposta = input("Cadastrar outro? (s/n) ")
    if resposta == 'n' : break  # encerra o laço

print(lista)
# CONTAR OS ITENS DE UMA LISTA
print(f"A lista tem {len(lista)} itens.")