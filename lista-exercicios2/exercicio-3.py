timeA = input("Digite o nome do seu time: ")
golsA = int(input("Digite a quantidade de gols do seu time: "))

timeB = input("Digite o nome do seu time: ")
golsB = int(input("Digite a quantidade de gols do seu time: "))

if golsA < golsB:
    print(timeB)
elif golsA > golsB:
    print(timeA)
elif golsA == golsB:
    print("Empate")