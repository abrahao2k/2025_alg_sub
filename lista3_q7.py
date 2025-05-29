'''7) Escreva um programa que pergunta o valor inicial
de uma dívida, a taxa mensal de juros e o valor 
que será pago a cada mês. Informe o número de meses
necessários para quitar a dívida, o total pago 
e quanto de juros foi pago.'''

divida_inicial = float(input("Divida inicial: "))
juros = float(input("Taxa de juros: "))
parcela = float(input("Parcela mensal: "))

divida = divida_inicial
mes = 0
pago = 0

while divida > 0 :
    if parcela > divida :         # última parcela
        pago = pago + divida    
        divida = 0
        
    else:
        divida = divida - parcela  # pagar a parcela
        divida = divida + (divida * juros / 100) # calcula juros
        pago = pago + parcela      # somar quanto ja pagou

    mes = mes + 1              # contar o mês
    
    print(f"Pagou {mes} parcela. Ainda deve R$ {divida:.2f}")
    
    
print(f"Pagou a dívida em {mes} meses.")
print(f"Total pago = R$ {pago:.2f}")
print(f"Juros = R$ {(pago-divida_inicial):.2f}")
    
    
    
    
