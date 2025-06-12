# continue - volta para o início do laço (linha do while)
# digitar as notas de 6 alunos e calcular a média
# da turma. se botar nota negativa, ignora.

aluno = 1
soma = 0
while aluno <= 6 :
    nota = float(input("Nota: "))
    if nota < 0 :  continue

    soma += nota
    print("nota registrada.")
    aluno += 1
    
print("Média = ", soma/6)



