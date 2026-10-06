# Conjunto: guarda valores únicos, sem repetir elementos e sem ordem fixa.
# Aqui vamos mostrar operações entre dois conjuntos: união, interseção e diferença.
A = {1, 2, 3}
B = {3, 4, 5}

print("União:", A | B)
print("Interseção:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Diferença simétrica:", A ^ B)
print("2 está em A?", 2 in A)