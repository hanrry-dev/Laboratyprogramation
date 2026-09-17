import random

numero = random.randint(1, 10)
palpite = int(input("palpite: "))

if palpite == numero:
    print("voce acertou!")
else:
    print("voce errou.")
    print("o numero era:", numero)
