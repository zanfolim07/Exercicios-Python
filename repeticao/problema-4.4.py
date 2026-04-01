nota = float(input("Nora: "))

#enquanto serve para sempre voltar e nao ficar repedindo o mesmo codigo
while nota < 0 or nota > 10:
    print("Nota invalida")
    nota = float(input("Digite novamente: "))

print(f"A nota inserida foi {nota} ")