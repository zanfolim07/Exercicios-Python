import math

numero = float(input("Numero:"))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadradada de {numero} é igual a {raiz}!")
else:
    print("Impossivel extrair raiz de numero negativo!")