total = 0

while True:
    numero = float(input("Digite uma nota ou 0 para encerrar: "))

    if numero == 0:
        break

    total = total + numero

print("Soma dos valores:", total)