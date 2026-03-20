rm = int(input("Digite o RM (5 dígitos): "))

digito1 = rm % 10
digito2 = (rm // 10) % 10
digito3 = (rm // 100) % 10
digito4 = (rm // 1000) % 10
digito5 = (rm // 10000) % 10

soma = digito1 + digito2 + digito3 + digito4 + digito5

print("--------Somatória do RM--------")
print("Dígitos:", digito5, "+", digito4, "+", digito3, "+", digito2, "+", digito1)
print("Soma total:", soma)