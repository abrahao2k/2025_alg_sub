'''9. Crie um programa que faz algumas perguntas
ao usuário e depois, usando um print 
formatado, exibe um pequeno texto biográfico.
Veja o exemplo:
Qual é o seu nome? João
Em que ano você nasceu? 1990
Qual o seu estado civil (casado, solteiro, etc.)? Casado
Em qual cidade você mora? Mossoró
João nasceu em 1990, é casado e mora em Mossoró
'''
nome = input("Qual é o seu nome? ")
ano  = input("Em que ano você nasceu? ")
estado = input("Qual o seu estado civil? ")
cidade = input("Em qual cidade você mora? ")

print(f"{nome} nasceu em {ano}, é {estado} e mora em {cidade}.")
