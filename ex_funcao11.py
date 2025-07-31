'''11.Modifique o programa anterior para escrever,
por extenso, números de 1 até 100.'''

def extenso(num):
    unidades   = ["","um","dois","tres","quatro","cinco",
                 "seis","sete","oito","nove"]
    
    especiais = ["dez","onze","doze","treze","catorze",
                 "quinze","dezesseis","dezessete",
                 "dezoito","dezenove"]
    
    dezenas = ["","","vinte","trinta","quarenta","cinquenta",
               "sessenta","setenta","oitenta","noventa"]
    
    if num < 1 or num > 100 :  print("Inválido")
    elif num == 100 :          print("Cem")
    elif 10 <= num <= 19 :     print(especiais[num - 10])
    elif num <= 9:             print(unidades[num])
    else:
        dezena  = num // 10  # quociente (inteiro)
        unidade = num % 10  # resto (inteiro)
        
        if unidade == 0 :
            print(dezenas[dezena])
        else:
            print(f"{dezenas[dezena]} e {unidades[unidade]}")

#########################
extenso(159)
extenso(100)
extenso(6)
extenso(13)
extenso(30)
extenso(57)
        