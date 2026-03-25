numA = int(input("Digite seu Primeiro numero:"))
operacao = input("Digite a operação (+, -, *, /): ")
numB = int(input("Digite seu Segundo numero:"))

if operacao == "+":
    print(numA + numB)
elif operacao == "-":
    print(numA - numB)
elif operacao == "*":
    print(numA * numB)
elif operacao == "/":
    if numB == 0:
        print("Impossível dividir por 0!")
    else:
        print(numA / numB)


