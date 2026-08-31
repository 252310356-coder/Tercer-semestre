# --- Primera Función: Multiplicacion heca con recursividad ---
def multiplicacion(x, y):
    if x > 0:
        # Se suma "y" a la multiplicacion hasta que "x" llegue a 0
        return y + multiplicacion(x - 1, y)
    else:
        #Retorna 0 cuando x llega a 0, cerrando la recursividad
        return 0

# Llamamos a la función pasando los valores de x y y para realizar la multiplicación
num_x = 4
num_y = 2
print(f"La multiplicacion de {num_x} x {num_y} es: {multiplicacion(num_x, num_y)}")


# --- Segunda Función: mostrar n cantidad de guiones dependiendo de la variable z ---
def guion(z):
    if z > 0:
        # Se concatena el guion actual con el resultado de la siguiente llamada recursiva
        return "-" + guion(z - 1)
    else:
        # Cuando z llega a 0, devuelve una cadena vacía para cerrar la recursión
        return ""

print(f"guiones: {guion(5)}")

# --- Tercera funcion: hacer una suma, considerando que x + y es igual a x + 1 + 1 + 1 ;. . . y cantidad de veces ---

def suma(x, y):
    if y > 0:
        # Se suma 1 a x y se resta 1 a y hasta que y llegue a 0, por lo tanto x se incrementa en y cantidad de veces
        return suma(x + 1, y - 1)
    else:
        return x

print(f"La suma de {num_x} + {num_y} es: {suma(num_x, num_y)}")

# --- Cuarta funcion: Potencia con recursividad, x es el numero y y es la potencia ---
def potencia(x, y):
    if y > 0:
        # Se multiplica x por el resultado de la siguiente llamada recursiva, disminuyendo y en 1 cada vez
        return x * potencia(x, y - 1)
    else:
        return 1

print(f"La potencia de {num_x} elevado a {num_y} es: {potencia(num_x, num_y)}")

# --- Quinta funcion: Va a hacer una suma de 0 siempre y cuando sea diferente de 1000
def suma_hasta_mil(x):
    if x != 1000:
        return x + suma_hasta_mil(x + 1)
    else:
        return 0

print(f"La suma de 0 hasta 1000 es: {suma_hasta_mil(0)}")