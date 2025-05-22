'''2) Modifique o programa anterior para solicitar a nota da
recuperação se o aluno ficou abaixo de 6. Calcule a 
média final usando a primeira média e a nota da recuperação.
O aluno será aprovado se a média final for 5 ou 
mais, caso contrário, será reprovado. Mostre a média
final e a mensagem
'''

n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))
n4 = float(input("Nota4: "))
media = (n1+n2+n3+n4)/4
print("A média é:", media)
 
if media >= 6:
    print("Aprovado.")
else:
    nota_rec = float(input("Nota recuperação: "))
    media_final = (media + nota_rec)/2
    print("Média final:", media_final)
    if media_final >= 5:
        print("Aprovado após recuperação.")
    else:
        print("Reprovado.")
    
    