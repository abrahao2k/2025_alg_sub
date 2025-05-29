'''6) Escreva um programa que pergunta o valor de
depósito inicial para uma poupança, e a taxa de 
rendimento mensal. Apresente o saldo dos próximos
24 meses, considerando o rendimento sobre 
o saldo atual de cada mês.'''

saldo = float(input("Deposito inicial? "))
taxa  = float(input("Taxa de rendimento? "))

mes = 1  # valor inicial

while mes <= 24 :  # teste lógico
    saldo = saldo + (saldo * taxa / 100)
    print(f"Mês {mes} = R$ {saldo:.2f}")
    mes = mes + 1 # incremento

