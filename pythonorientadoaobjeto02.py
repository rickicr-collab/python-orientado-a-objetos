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

p = Pessoa('Ana', 25) # orientação a objetos - encapsulamento
p.imprimir() # imprimir a variavel instancianda a objetos usando a função pré definida imprimir