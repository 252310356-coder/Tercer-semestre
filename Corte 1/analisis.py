print ("Forma bruta de resolverlo")

import random

# Generamos una caminata aleatoria (Random Walk) con 40,000 puntos para simular precios reales
random.seed(42)
precios = [100.0]
for _ in range(10000000):
  cambio = random.uniform(-1.5, 1.5)
  nuevo_precio = max(10.0, precios[-1] + cambio)  # Evitamos precios negativos
  precios.append(round(nuevo_precio, 2))


K = 20

def max_ganancia_fuerza_bruta(precios, k):
  max_g = 0
  n = len(precios)

  for i in range(n):
    # El día de venta no puede exceder i + k días
    limite = min(n, i + k + 1)
    for j in range(i + 1, limite):
      ganancia = precios[j] - precios[i]
      if ganancia > max_g:
        max_g = ganancia

  return max_g
print(max_ganancia_fuerza_bruta (precios, K))


# Ejemplo de uso:
# precios = [7, 1, 5, 3, 6, 4], k = 2
# print(max_ganancia_fuerza_bruta([7, 1, 5, 3, 6, 4], 2))

print ("Uso de Min Heap")
import heapq


def max_ganancia_heap(precios, k):
  max_g = 0
  min_heap = []  # Almacena tuplas: (precio, dia)

  for j, precio_actual in enumerate(precios):
    # Eliminar elementos que están fuera de la ventana de K días
    while min_heap and min_heap[0][1] < j - k:
      heapq.heappop(min_heap)

    # Si hay elementos en la ventana, calculamos la ganancia con el precio mínimo
    if min_heap:
      precio_minimo = min_heap[0][0]
      ganancia = precio_actual - precio_minimo
      if ganancia > max_g:
        max_g = ganancia

    # Añadir el precio actual al heap
    heapq.heappush(min_heap, (precio_actual, j))

  return max_g
print(max_ganancia_heap (precios, K))

print ("Cola monotona")

from collections import deque


def max_ganancia_deque(precios, k):
  max_g = 0
  dq = deque()  # Almacena índices de los precios

  for j, precio in enumerate(precios):
    # Remover índices que ya quedaron fuera de la ventana de K días
    if dq and dq[0] < j - k:
      dq.popleft()

    # Mantener la cola monótona eliminando elementos mayores que el actual
    while dq and precios[dq[-1]] >= precio:
      dq.pop()

    dq.append(j)

    # El precio mínimo de la ventana actual siempre está al frente
    precio_minimo = precios[dq[0]]
    ganancia = precio - precio_minimo
    if ganancia > max_g:
      max_g = ganancia

  return max_g

print (max_ganancia_deque (precios, K))