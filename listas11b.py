cores = ['Verde','Cinza','Amarelo','Azul','Branco','Cinza']
            #0      #1      #2       #3      #4      #5
print(cores)

# REMOVER INDICANDO A POSIÇÃO 
pos = int(input("Digite a posição: "))

if pos < len(cores) :
    print("Estou removendo " + cores.pop(pos) )
else:
    print("Posição inválida.")

print(cores)