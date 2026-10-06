# Busca binária: compara o valor do meio e elimina metade da lista.
# Se o valor do meio for maior que o item, procura na esquerda; se for menor, procura na direita.
def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) - 1

  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute == item:
      return meio
    elif chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None

numeros = [3, 8, 15, 23, 42, 56, 78]
print(pesquisa_binaria(numeros, 42))
