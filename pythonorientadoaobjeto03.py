class Pessoa:
    def __init__(self, nome, idade): # construtor
        self.nome = nome # atributos 
        self.idade = idade # atributos 
    def imprimir (self): # Operações ou (metodos)
        print(self.nome, 'tem',
              self.idade, 'anos(s)')
    def getIdade(self): # tipo & variavel - Função GETTERS para encapsulamento
        return self.idade
    def setIdade(self, idade): # classe e objeto - Função SETTERS para encapsulamento
        self.idade = idade


class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print('E trabalha como', self.profissao)

p = Pessoa('Ana', 25) 
p = Profissional('Ana', 25, 'balconista')
p.imprimir()   

        