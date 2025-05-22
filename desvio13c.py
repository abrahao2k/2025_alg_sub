v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
op = input("Qual operação? (+, -, *, /) : ")

if op == "+" :
    print("Soma = ", v1+v2)
elif op == "-" :
    print("Subtração = ", v1-v2)
elif op == "*" :
    print("Multiplicação = ", v1*v2)
elif op == "/" :
    print("Divisão = ", v1/v2)
else:
    print("Operador inválido.")