iptu = float(input("Digite seu IPTU: "))

desconto = iptu * 3 /100
aVista = iptu - desconto

parcelado = iptu / 10

print("------IPTU 2026------")
print("Valor Total:     R$", iptu)
print("Desconto (3%):     R$", desconto)
print("Seu valor a vista é:     R$", aVista)
print("Seu valor com 10 parcelas é:     R$", parcelado)