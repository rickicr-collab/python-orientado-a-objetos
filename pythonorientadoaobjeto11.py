# ------- Herança --------#
# Exemplo 02
# herança Multipla 
# Não é aplicado é apenas para mostrar uma aplicação de herança multipla pois apresenta erros na execução( apenas uso de estudo)
import datetime
class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        
class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo, limite):
        Conta.__init__(self, cliente, numero, saldo) # opcional super() - no entanto não é recomendado em caso de herança multipla 
        self.limite = limite
    def sacar(self, valor):
        if (self.sacar + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SACAR', valor])
            return True
class Poupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()
    def remuneraConta(self):
        self.saldo += self.saldo * self.taxaremuneracao
        
    def __init__(self, cliente, numero, saldo, taxaremuneracao, limite):
        Conta.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxaremuneracao)
        ContaEspecial.__init__(self, limite)
        self.taxaremuneracao = taxaremuneracao
    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)

cx = ContaRemuneradaPoupanca ([c1, c2], 98939123, 1500.00, 0.3)
cx.remuneraConta()
print(cx.saldo)
    