
# -----Metodo de Classe ------#
class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    # Padrão FActory
    @classmethod
    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(' '))
        objeto = cls(nome, sobrenome)
        return objeto
registro1 = NomeCompleto.fromString('Luiz Braga') 
        