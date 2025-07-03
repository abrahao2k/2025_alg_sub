# LISTAS ANINHADAS (LISTA DENTRO DE LISTA)

aluno1 = ['Ana Maria', 10]
aluno2 = ['Cláudio', 7.5]
aluno3 = ['Fabiana', 9.6]
aluno4 = ['Marcio', 8.2]

turma = [aluno1, aluno2, aluno3, aluno4]
           #0      #1      #2      #3

print(turma)     # imprime a lista com todas as sub-listas
print(turma[2])  # imprime a sub-lista da posição indicada

# só o nome do aluno
print(turma[1][0]) # imprime um elemento da sub-lista indicada
