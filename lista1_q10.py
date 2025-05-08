'''10) O cardápio de uma lanchonete é dado abaixo.
Prepare um algoritmo que leia a quantidade de cada
item que você consumiu e calcule a conta final. 
Hambúrguer................. R$ 8,00 
Cheeseburger............... R$ 10,50 
Fritas............................ R$ 6,50 
Refrigerante................. R$ 5,00 
Milkshake..................... R$ 13,00'''

hamb = int(input("Qtd. Hamburguer: "))
chee = int(input("Qtd. Cheeseburger: "))
frit = int(input("Qtd. Fritas: "))
refr = int(input("Qtd. Refrigerante: "))
milk = int(input("Qtd. Milkshake: "))

total = hamb*8.00 + chee*10.50 + frit*6.50 + refr*5.00 + milk*13.00
print(f"Total da conta: R$ {total:.2f}")