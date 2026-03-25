dias_uteis = int(input("Digite o total de dias úteis do mês: "))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora de trabalho: R$ "))

jornada_normal = dias_uteis * 8

if horas_trabalhadas > jornada_normal:
    horas_extras = horas_trabalhadas - jornada_normal
    valor_hora_extra = valor_hora * 1.5

    salario = (jornada_normal * valor_hora) + (horas_extras * valor_hora_extra)

    print(f"Horas extras: {horas_extras:.0f}h")
    print(f"Salário com hora extra: R$ {salario:.2f}")
else:
    salario = horas_trabalhadas * valor_hora
    print("Sem horas extras")
    print(f"Salário: R$ {salario:.2f}")