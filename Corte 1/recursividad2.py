def suma_iterativa(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def suma_recursiva(n):
    # 3. Condición de salida (caso base)
    if n == 0:
        return 0
    # 2. Segmento recursivo
    else:
        return n + suma_recursiva(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    # 3. Condición de salida (caso base)
    if n == 0 or n == 1:
        return 1
    # 2. Segmento recursivo
    else:
        return n * factorial_recursivo(n - 1)

def potencia_iterativa(base, exp):
    resultado = 1
    for _ in range(exp):
        resultado *= base
    return resultado

def potencia_recursiva(base, exp):
    # 3. Condición de salida (caso base)
    if exp == 0:
        return 1
    # 2. Segmento recursivo
    else:
        return base * potencia_recursiva(base, exp - 1)

def conteo_iterativo(n):
    for i in range(n, -1, -1):
        print(i)

def conteo_recursivo(n):
    # 3. Condición de salida (caso base)
    if n < 0:
        return
    print(n)
    # 2. Segmento recursivo
    conteo_recursivo(n - 1)

def suma_lista_iterativa(lista):
    total = 0
    for num in lista:
        total += num
    return total

def suma_lista_recursiva(lista):
    # 3. Condición de salida (caso base)
    if len(lista) == 0:
        return 0
    # 2. Segmento recursivo
    else:
        return lista[0] + suma_lista_recursiva(lista[1:])

print("Suma iterativa de 5:", suma_iterativa(5))
print("Suma recursiva de 5:", suma_recursiva(5))

print("Factorial iterativo de 5:", factorial_iterativo(5))
print("Factorial recursivo de 5:", factorial_recursivo(5))

print("Potencia iterativa de 2^3:", potencia_iterativa(2, 3))
print("Potencia recursiva de 2^3:", potencia_recursiva(2, 3))

print("Conteo iterativo desde 5:")
conteo_iterativo(5)
print("Conteo recursivo desde 5:")
conteo_recursivo(5)

print("Suma de lista iterativa [1, 2, 3, 4, 5]:", suma_lista_iterativa([1, 2, 3, 4, 5]))
print("Suma de lista recursiva [1, 2, 3, 4, 5]:", suma_lista_recursiva([1, 2, 3, 4, 5]))

