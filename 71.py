class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0


class Banco:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self):
        nome = input("Nome do usuario: ")
        self.usuarios.append(Usuario(nome))
        print(f"Usuario criado. Codigo: {len(self.usuarios) - 1}")

    def depositar(self):
        codigo = int(input("Codigo do usuario: "))
        valor = float(input("Valor do deposito: "))
        self.usuarios[codigo].saldo += valor

    def sacar(self):
        codigo = int(input("Codigo do usuario: "))
        valor = float(input("Valor do saque: "))
        usuario = self.usuarios[codigo]

        if valor > usuario.saldo:
            print("Saldo insuficiente")
            return

        usuario.saldo -= valor

    def mostrar_resumo(self):
        codigo = int(input("Codigo do usuario: "))
        usuario = self.usuarios[codigo]
        print(f"Nome: {usuario.nome}\nSaldo: R$ {usuario.saldo:.2f}")

    def listar_usuarios(self):
        for codigo, usuario in enumerate(self.usuarios):
            print(f"{codigo}: {usuario.nome}")


banco = Banco()
banco.adicionar_usuario()
banco.listar_usuarios()
banco.mostrar_resumo()
banco.depositar()
banco.sacar()
banco.mostrar_resumo()