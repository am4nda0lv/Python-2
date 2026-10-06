# Busca sequencial: percorre a lista e retorna a posição do item quando o encontra.
# O enumerate entrega o índice e o valor de cada elemento.
def pesquisa_sequencial(lista, item):
  for i, j in enumerate(lista):
    if j == item:
      return i
  return -1

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
print(pesquisa_sequencial(numeros, 30))