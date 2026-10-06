# Busca binária: olha o valor do meio e descarta metade da lista.
# Se o meio for menor que o item, o item está à direita; se for maior, está à esquerda.
# Exemplo: lista [3, 8, 15, 23, 42, 56, 78], item 42 -> meio = 23, depois 56, depois 42.
def pesquisa_binaria(lista, item):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        if lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

numeros = [3, 8, 15, 23, 42, 56, 78]
print(pesquisa_binaria(numeros, 42))