# ------Execessoes -------#
# exemplo 01
x = 10
if x > 5:
    # ao executar essa condição a raise está informando que é para subir essa exceção eimprimir a mensagem indicada
    raise Exception('x não pode ser mais que 5. O valor de x foi de {}'.format(x))