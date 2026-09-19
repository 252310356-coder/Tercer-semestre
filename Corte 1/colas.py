from collections import deque
#Crear las 3 pilas que se van a usar
pila1 = deque()

pila2 = deque()

pila3 = deque()

#Agregar datps a la pila 1 y a la pila 2
pila1.append(1)
pila1.append(5)
pila1.append(3)
pila1.append(7)
pila1.append(9)

pila2.append(2.6)
pila2.append(4.8)
pila2.append(6.0)
pila2.append(8.2)
pila2.append(10.4)

#Definir la variable suma
suma = 0
#Repetir el ciclo segun la longitud de la pila 1 y sumar los elementos de la pila 1
for i in range(len(pila1)):
    suma += pila1.pop()

print("La suma de los elementos de la pila 1 es:", suma)

#Definir la variable producto
producto = 1
#Repetir el ciclo segun la longitud de la pila 2 y multiplicar los elementos de la pila 2
for i in range(len(pila2)):
    elemento = pila2.pop()
    producto *= elemento
    pila3.append(producto)

#Mostrar los elementos de la pila 3 y el producto de los elementos de la pila 2
print("El producto de los elementos de la pila 2 es:", producto)
print("Los elementos de la pila 3 son:", list(pila3))