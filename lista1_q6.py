'''6) Em uma eleição sindical concorreram ao cargo de
presidente três candidatos (A, B e C). Durante a apuração 
dos votos foram computados votos nulos e votos em branco,
além dos votos válidos para cada candidato. Deve 
ser criado um programa de computador que efetue a leitura
da quantidade de votos válidos para cada 
candidato, além de efetuar também a leitura da quantidade
de votos nulos e votos em branco. Ao final o 
programa deve apresentar o número total de eleitores,
considerando votos válidos, nulos e em branco; o 
percentual correspondente de votos válidos em relação à
quantidade de eleitores; o percentual correspondente 
de votos válidos de cada candidato em relação à quantidade
de eleitores, além do percentual de votos brancos 
e votos nulos; '''

CAND_A = int(input("Votos Candidato A: "))
CAND_B = int(input("Votos Candidato B: "))
CAND_C = int(input("Votos Candidato C: "))
BRANCO = int(input("Votos em Branco: "))
NULO   = int(input("Votos Nulos: "))

TOTAL = CAND_A + CAND_B + CAND_C + BRANCO + NULO
print("Total de Eleitores:", TOTAL)

print(f"Candidato A: {CAND_A / TOTAL * 100:.1f}%")
print(f"Candidato B: {CAND_B / TOTAL * 100:.1f}%")
print(f"Candidato C: {CAND_C / TOTAL * 100:.1f}%")
print(f"Brancos: {BRANCO / TOTAL * 100:.1f}%")
print(f"Nulos: {NULO / TOTAL * 100:.1f}%")







