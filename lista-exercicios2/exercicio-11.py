print("------ Media final python -----")
media1 = int(input("Digite sua media do primeiro semestre: "))
media2 = int(input("Digite sua media do segundo semestre: "))
frequencia = int(input("Digite sua Frequencia: "))

mediaPrimeiroSemestre = media1 * 4
mediaSegundoSemestre = media2 * 6

if frequencia <= 70:
    print("Reprovado por ausencia")
else:
    mediaFinal = (mediaPrimeiroSemestre + mediaSegundoSemestre) / 10
    if mediaFinal >= 7:
        print("Aprovado")
    elif 5 <= mediaFinal <= 6.9:
        print("Exame")
    else:
        print("Reprovado por nota")
print("------ final -----")