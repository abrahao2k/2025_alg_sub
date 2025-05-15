# O programa pergunta a idade do usuário, se tem
# carteira de motorista e se tem veículo.
# Diz que pode dirigir se tem 18 anos
# ou mais e carteira e veiculo.

idade = int(input("Qual a idade? "))
carteira = input("Tem carteira de motorista? (s/n) ")
veiculo = input("Tem veículo? (s/n) ")

if idade >= 18 and carteira == "s" and veiculo == "s":
    print("Você pode dirigir.")
else:
    print("Não pode dirigir.")