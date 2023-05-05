# ------- Polimorfismo -----------#
# Exemplo 01
# classe criada nome argentina 
class Argentina():
    def capital(self): # função capital na classe argentina
        print('Buenos Aires é a capital da Argentina.');
    def lingua_oficial(self): # função lingua oficial na classe argentina
        print('A lingua oficial da Argentina é o espanhol.')
# Classe Criada nome Brasil        
class Brasil():
    def capital(self): # funçõa capital na classe brasil 
        print('Brasilia é a capital do Brasil.')
    def lingua_oficial(self): # função lingua oficial na classe brasil 
        print('A lingua oficial do Brasil é o portugues.')
 
 # atribuindo objetos as suas respectivas classes Argentina e Brasil        
obj_arg = Argentina()
obj_bra = Brasil()
# criando um laçõ For com comprimento objetos obj_arg, obj_bra 
for pais in (obj_arg, obj_bra):
    pais.capital() # chamando a função capital para ambos os objetos 
    pais.lingua_oficial() # chamando a função lingua oficial para ambos os objetos
        
    