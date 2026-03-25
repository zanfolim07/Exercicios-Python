gols_time_a = int(input("Gols Time A: "))
gols_time_b = int(input("Gols Time B: "))

if gols_time_a > gols_time_b:
    print("Time A Venceu a partida:")
    print(f"{gols_time_a} X {gols_time_b}")
elif gols_time_a < gols_time_b:
    print("Time B Venceu a partida:")
    print(f"{gols_time_a} X {gols_time_b}")
else:
    print("Empate entre os times")
    print(f"{gols_time_a} X {gols_time_b}")

print("Fim do Programa")