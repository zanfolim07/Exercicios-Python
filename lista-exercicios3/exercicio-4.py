n = int(input("Digite a quantidade de números: "))

positivo = 0
negativo = 0
contador = 0

while contador < n:
    numero = float(input("Digite um número: "))
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

    contador += 1

print("Quantidade de positivos:", positivo)
print("Quantidade de negativos:", negativo)