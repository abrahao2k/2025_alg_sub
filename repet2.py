# digite um valor, mostre o dobro do valor.
# pergunte se quer calcular outra vez e repita

resp = "s"                                      # VALOR INICIAL

while resp == "s":                              # TESTE LÓGICO
    num = int(input("Digite um número: "))
    print(f"O dobro de {num} é {num*2}")
    
    resp = input("Calcular outro? (s/n) ")      # INCREMENTO (MUDANÇA)

