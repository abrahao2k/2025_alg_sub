# CRIE UMA LISTA VAZIA, FAÇA UM LAÇO PARA CADASTRAR
# VARIOS ITENS NESSA LISTA. AO FINALIZAR OS CADASTROS
# IMPRIMA MENSAGENS DIZENDO O CONTEÚDO DE CADA POSIÇÃO
# EX.:
# Posição 0 - Batata
# Posição 1 - Pastel
# Posição 2 - Nescau

lista = []

while True:
    lista.append(input("Digite o item: "))
    resp = input("Outro? (s/n) ")
    if resp == 'n' : break

posicao = 0
while posicao < len(lista):
    print(f"Posição {posicao} - {lista[posicao]}")
    posicao += 1
    
    
    
    