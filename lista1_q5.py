'''5) Ler o valor correspondente ao salário mensal
(variável SM) de um trabalhador e também o valor do
percentual de reajuste (variável PR) a ser atribuído.
Apresentar o valor do novo salário (variável NS).'''

salario = float(input("Salário atual: "))
reajuste = float(input("Percentual reajuste: "))

novo = salario + (salario * reajuste/100 )

print(f"Novo salário: R$ {novo:.2f}")

