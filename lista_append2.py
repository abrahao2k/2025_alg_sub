'''Crie um programa que permita ao usuário inserir suas notas
(em valores reais/float) em uma lista usando um loop "while".
Quando o usuário inserir um valor negativo, o programa deve
parar de solicitar notas. Em seguida, calcule a média das notas e 
exiba-a na tela.'''

notas = []
n = 0
while n >= 0 :
    n = float(input("Digite a nota: "))
    if n >= 0 : notas.append(n)

### fora do laço - calcular a média ###
# sum - soma os itens de uma lista
# len - conta a quantidade de itens de uma lista

print("Média = ", sum(notas) / len(notas) )



