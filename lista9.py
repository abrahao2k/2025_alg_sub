cores = ['Verde','Cinza','Amarelo','Azul','Branco','Cinza']
            #0      #1      #2       #3      #4      #5
print(cores)

#VERIFICAR SE UM ELEMENTO EXISTE NA LISTA
cor = input("Digite uma cor: ")

if cor in cores :
    print('Achei a cor indicada.')
else:
    print('Não achei essa cor.')