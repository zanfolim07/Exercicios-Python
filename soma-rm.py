num = int(input("Digite seu rm de 5 digitos: "))
soma = 0

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

print("A soma vale: ", soma)