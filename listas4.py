# PERCORRER UMA LISTA ITEM POR ITEM USANDO WHILE

nomes = ['Abel','Caio','Diana','Fernando','Lara']
           #0     #1     #2        #3       #4

posicao = 0
while posicao < len(nomes) :
    print(f"Seja bem vindo, {nomes[posicao]}!")
    posicao += 1
