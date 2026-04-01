soma = 0

numero = int(input("Digite um numero (0 para parar): "))

while numero != 0:
    if numero % 2 == 0:
        soma += numero

    numero = int(input("Digite um numero (0 para parar): "))

print("A soma dos numeros pares é:", soma)