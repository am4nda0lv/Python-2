# Lista: estrutura que guarda vários itens em sequência.
# Neste exemplo, acessamos o sexto elemento da lista e depois o primeiro item da lista interna.
x = [1, 5, 3, "b", "a", [True, False]]
# Retorna o sexto elemento da lista e o primeiro da lista aninhada
print(x[5][0])