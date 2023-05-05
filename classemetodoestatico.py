# ----- Metodo estatico --------#
class NomeCompleto:
    def __init__ (self, nome , sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @staticmethod
    def isValid(texto):
        nomes = texto.split(' ')
        return len(nomes) > 1

NomeCompleto.isValid()