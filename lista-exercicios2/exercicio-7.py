idade = int(input("Digite a idade do nadador: "))

print("Categoria    | Idade")
print("-------------|----------")


if idade >= 5 and idade <= 7:
    print("Infantil     | ", idade)
elif idade >= 8 and idade <=10:
    print("Juvenil     | ", idade)
elif idade >=11 and idade <= 15:
    print("Adolecente     | ", idade)
elif idade >=16 and idade <= 30:
    print("Adulto     | ", idade)
elif idade >30:
    print("Senior     | ", idade)

