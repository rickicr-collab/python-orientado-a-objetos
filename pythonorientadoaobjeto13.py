# ------ Tratamento de exceções --------#
# exemplo 02
x = 0
try:
    print(x)
except:
    print('variavel Indefinida')

# ----------------------------#
#exemplo 03
class ExcecaoCustomizada:
    pass

x = -1
if x < 0:
    raise Exception('Valor Negativo!!!')

x = 'Hello'
if not type(x) is int:
    raise TypeError('Use apenas inteiros')
