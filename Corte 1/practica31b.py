from collections import deque

from numpy import double

pila = deque()

# Pedir elementos hasta que usuario ingrese "fin"
while True:
    elemento = input("Ingrese un elemento (o 'fin' para terminar): ")
    elemento = double(elemento)  # Convertir a tipo double
    if elemento == "fin":
        break
    pila.append(elemento)

print("Pila después de apilar elementos:", pila)