# ------- Agregação ---------#
class Conta:
    def __init__ (self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar (self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
class Cliente:
    def __init__ (self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
# ----- Composição --------#
class Extrato:
    def __init__ (self):
        self.transacoes = []
    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])
class Conta:
    def __init__ (self,clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITAR', valor])
    def sacar(self):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor])
            return True
valor = 0
c1 = Cliente('Carlos', '111111111-11', 'Rua das Marrecas')
c2 = Cliente('Ana', '222222222-22','Rua dos Girassois')

conta = Conta([c1, c2],24237891,2500.00)
conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()