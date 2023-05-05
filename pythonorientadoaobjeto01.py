
class Pessoa:
    def __init__(self, nome, ender): #construtor da classe pessoa usando __init__
        self.set_nome(nome) # atribuindo parametro nome usando parametro base self
        self.set_ender(ender) # atribuido endereço usando paramentro base self 
        
    def set_nome(self, nome): # definindo parametro nome a uma constante nome
        self.nome = nome
        
    def set_ender(self, ender): # definindo paramentro ender a uma constante endereço
        self.ender = ender
        
    def get_nome(self): # aqui realizando o retorno do paramentro constante  nome na classe Pessoa
        return self.nome
    
    def get_ender(self): # aqui realizando o retorno do parametro constante endereço na classe Pessoa
        return self.ender
     
pessoa1 = Pessoa('Maria','Rua 01234') # variavel pessoa1 atribuido com valores nome e endereço
pessoa2 = Pessoa('João','Rua 56789') # variavel pessoa2 atribuido com valores nome e endereço


print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}') #imprimir os valores de pessoa1
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}') # imprimir os valores de pessoa2
