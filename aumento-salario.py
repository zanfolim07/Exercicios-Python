salario = float(input("Digite seu salario atual: "));
aumento = float(input("Digite seu percentual de aumento:"));

percentual = salario * aumento / 100
novoSalario = salario + percentual

print("--------Aumento Salarial--------")
print("Seu salario antigo: ", salario)
print("Seu percentual: ", percentual)
print("Seu salario atual: ", novoSalario)