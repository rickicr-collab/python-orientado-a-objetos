# ------- Polimorfismo ----------#
# Exemplo 02
# classe veiculo criada
class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustivel.')
        
# classe Veiculo eletrico criada - herdando propriedades da classe veiculo         
class VeiculoEletrico(Veiculo): # parametro veiculo significando heranca da classe pai
    def rodar(self): # função rodar 
        super().rodar() # chamando a função rodar herdade da classe pai veiculo
        print('Esse veiculo utiliza eletricidade.')
        
veiculo_eletrico = VeiculoEletrico() # instanciando o objeto veiculo_eletrico a classe VeiculoEletrico
veiculo_eletrico.rodar() # chamando o objeto veiculoeletrico com a função rodar herdada da classe pai Veiculo