setor1 = float(input("consumo setor 1: "))
setor2 = float(input("consumo setor 2: "))

if setor1 > setor2:
    print("O setor 1 teve o maior consumo.")
elif setor2 > setor1:
    print("O setor 2 teve o maior consumo.")
else:
    print("Os dois setores tiveram o mesmo consumo.")