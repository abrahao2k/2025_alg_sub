'''1 - Crie uma lista de nomes e peça ao usuário para inserir um nome.
Use um loop while para verificar se o nome está na lista. Se estiver,
exiba "Nome encontrado!", caso contrário, continue pedindo 
nomes.'''

nomes = ['Ana','Beto','Claudia','Diego','Fernanda','Gabriel','Helena',
         'Ivo','Juliana','Kaio','Lucia','Mario','Noeli','Otavio']

pesquisa = ""

while pesquisa not in nomes:
    pesquisa = input("Digite um nome: ")
    
    if pesquisa in nomes:
        print("Nome encontrado.")
    else:
        print("Esse nome não está na lista.")
        
        
        