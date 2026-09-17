produtos = {}

for i in range(3):
    nome = input("produto: ")
    quantidade = int(input("quantidade: "))
    produtos[nome] = quantidade

print(produtos)
