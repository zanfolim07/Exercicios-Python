valor = float(input("Digite o valor da etiqueta: "))

print("1 - A vista em dinheiro ou cheque")
print("2 - A vista no cartão de crédito")
print("3 - Em duas vezes")
print("4 - Em quatro vezes")

opcao = int(input("Digite o número da forma de pagamento: "))

if opcao == 1:
    print(f"Total com desconto: R$ {valor * 0.90:.2f}")
elif opcao == 2:
    print(f"Total com desconto: R$ {valor * 0.95:.2f}")
elif opcao == 3:
    print(f"Duas parcelas de: R$ {valor / 2:.2f}")
elif opcao == 4:
    total = valor * 1.07
    print(f"Quatro parcelas de: R$ {total / 4:.2f}")