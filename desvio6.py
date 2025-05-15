tempo = int(input("Digite o tempo (em minutos): "))
veiculo = input("Qual veículo (moto/carro): ")

if tempo <= 10 :
    print("Estacionamento grátis!")

else:
    if veiculo == "moto" :
        print("Tarifa: R$ 1,50")
    else:
        print("Tarifa: R$ 3,00")

