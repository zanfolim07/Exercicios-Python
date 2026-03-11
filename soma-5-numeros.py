#leia 5 numeros 

#input é para string
aux = input("Primeiro numero: ")
num1 = int(aux) #funcao int() converte uma string para int

aux = input("Segundo numero: ")
num2 = int(aux) 

aux = input("Terçeiro numero: ")
num3 = int(aux)

aux = input("Quarto numero: ")
num4 = int(aux)

aux = input("Quinto numero: ")
num5 = int(aux)

soma = num1 + num2 + num3 + num4 + num5 
print("A soma vale", soma)