# Acumulador: guarda a soma dos valores enquanto o loop executa.
# Aqui, a variável soma vai somando cada número até chegar em 15.
x = 1
soma = 0
while x <= 5:
  soma += x
  x += 1
print(f"Soma: {soma}")