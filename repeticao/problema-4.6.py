num = int(input("Digite numero: "))

div = 1

while div <= num:
    if num % div == 0:
        print(div)
    div = div + 1
