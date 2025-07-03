cores = ['Verde','Cinza','Amarelo','Azul','Branco']
            #0      #1      #2       #3      #4

# POSIÇÃO DE UM ELEMENTO NA LISTA
cor = input("Digite uma cor: ")

if cor in cores:
    print(f"{cor} está na posição {cores.index(cor)}")
else:
    print(f"{cor} não está na lista.")