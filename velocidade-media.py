# calcula a velocidade média em m/s e em km/h de um corredor

distancia = int(input("Digite a distancia em metros : "))
tempo = int(input("Digite o tempo em segundos: "))

minutosPorSegundo = distancia / tempo
quilometrosPorHora = minutosPorSegundo * 3.6 

print("----------Calculo----------")
print("Velocidade media em m/s: ", minutosPorSegundo)
print("Velocidade media em km/h: ", quilometrosPorHora)