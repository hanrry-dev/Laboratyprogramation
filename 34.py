alunos = {
    "Ana": 8.5,
    "Carlos": 7.0,
    "Pedro": 9.0
}

nome = input("nome do aluno: ")

if nome in alunos:
    print("nota:", alunos[nome])
else:
    print("aluno não encontrado.")
