
peso = float(input("Informe o seu peso(kg): "))
altura = float(input("Informe sua altura(m): "))
imc = peso / (altura * altura)
if imc >= 30:
    print(f"O seu IMC é de '{imc}'. O seu quadro é de obsidade.")
elif imc >= 25:
    print(f"O seu IMC é de '{imc}'. O seu quadro é de sobrepeso. ")
