vogais = 0
VOGAIS = "aeiouAEIOU"

Palavra = str(input("Digite uma palavra:"))

for i in Palavra:
    if Palavra == VOGAIS:
        vogais += 1
    print(f'A palavra "{Palavra}" tem {vogais} vogais')