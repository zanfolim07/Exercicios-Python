dia = int(input("Digite seu dia: "))
mes = int(input("Digite seu mes: "))
ano = int(input("Digite seu ano: "))

if mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        valido = 1 <= dia <= 29
    else:
        valido = 1 <= dia <= 28
elif mes in [4, 6, 9, 11]:
    valido = 1 <= dia <= 30
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    valido = 1 <= dia <= 31
else:
    valido = False

if valido:
    print("A data é valida!")
else:
    print("A data é invalida!")