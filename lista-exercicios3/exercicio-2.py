n = int(input("Digite o número de alunos: "))

soma = 0
contador = 0

while contador < n:
    nota = float(input(f"Digite a nota do aluno {contador + 1}: "))
    soma += nota
    contador += 1  

media = soma / n

print("A média da turma é:", media)