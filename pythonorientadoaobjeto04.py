# Atributos
class Pessoa: 
    _contador = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1
    def imprimir(self):
        print(self.nome, 'tem',
              self.idade,'anos(s)')
    # Propriedades
    @property 
    def contador(self):
        return type(self)._contador
#atributos estaticos    
p1 = Pessoa('Carlos', 18) # variavel p1 sendo um objeto instanciado a classe pessoa 
print(p1.contador)
print(Pessoa._contador) # contador realizando a adição dos objetos adicionados e instanciados dentro da classe pessoa 
p1.imprimir()
