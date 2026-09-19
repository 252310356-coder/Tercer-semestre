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

pila_invertida = [ ]
while pila:
    pila_invertida.append(pila.pop())

print("Pila después de apilar elementos:", pila)
print("Pila invertida:", pila_invertida)

#Programa para verificar si una palabra es un palindromo
# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")
# Extraer cada caracter de la palabra y apilarlo en otra pila
pila_caracteres = deque()
for caracter in palabra:
    pila_caracteres.append(caracter)

# Formar la nueva palabra a partir de los caracteres apilados
palabra_invertida = ""
while pila_caracteres:
    palabra_invertida += pila_caracteres.pop()

# Comparar la palabra original con la nueva palabra formada
if palabra == palabra_invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")