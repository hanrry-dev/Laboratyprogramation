import random

numero = random.randint(1, 10)

while True:
    palpite = int(input("palpite: "))

    if palpite == numero:
        print("voce acertou!")
        break
    elif palpite < numero:
        print("o numero procurado é maior.")
    else:
        print("o numero procurado é menor.")
