from collections import deque

pila = deque()

# Pedir elementos hasta que usuario ingrese "fin"
while True:
    elemento = input("Ingrese un numero (escribir 'fin' para terminar): ")
    elemento = (elemento)
    if elemento == "fin":
        break
    pila.append(elemento)

print("Pila después de apilar elementos:", pila)
pila_invertida = [ ]
while pila:
    pila_invertida.append(pila.pop())

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