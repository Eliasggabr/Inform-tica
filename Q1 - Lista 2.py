soma = 0 

for i in range(3):
    Notas = int(input(f"Digite a {i+1}ª nota do aluno: "))
    soma += Notas
soma_media = soma / (i+1)
print(f"A média das notas é: {soma_media}")
if soma_media >= 7:
   print("Aprovado")
else:
   print("Reprovado")