preco = float (input("Preço:"))
descontopercentual = float (input("Desconto:"))

desconto = preco * descontopercentual  / 100
preco_final = preco - desconto
print(preco_final)

