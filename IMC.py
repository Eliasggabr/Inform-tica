
peso = float(input)("Digite seu peso em kg: ")
altura = float(input)("Digite sua altura em metros: ")
imc = peso / (altura * altura)
if imc >= 30:
    print("Obesidade")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")