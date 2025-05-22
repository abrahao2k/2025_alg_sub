# REPETIÇÃO - CONDIÇÃO MÚLTIPLA - OR
# o programa aceita diversos votos nos candidatos A e B
# se escolher um candidato inexistente, encerra a repetição
# diz quantos votos cada um recebeu, e quem ganhou
votos_A = 0
votos_B = 0

cand = "A"  # valor inicial

while cand == "A" or cand == "B" :   # teste lógico
    cand = input("Escolha o candidato (A/B): ") # incremento (mudança)
    if   cand == "A" : votos_A = votos_A + 1
    elif cand == "B" : votos_B = votos_B + 1
    else: print("Candidato inválido.")

else:
    print(f"Votos A = {votos_A} / Votos B = {votos_B}")
    if   votos_A > votos_B : print("Candidato A venceu.")
    elif votos_B > votos_A : print("Canditado B venceu.")
    else: print("EMPATE!")
    