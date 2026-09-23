from collections import deque
def verificar_parentesis(expresion):
    # Crear una pila vacía utilizando deque
    pila = deque()
    #Recorrer cada carácter en la expresión
    for caracter in expresion:
        #Si el carácter es un paréntesis de apertura, se agrega a la pila
        if caracter == "(" or caracter == "{" or caracter == "[" or caracter == "<":
            pila.append(caracter)
        #Si el caracter es un parentesis de cierre, verifica que haya uno de apertura en la pila
        elif caracter == ")" or caracter == "}" or caracter == "]" or caracter == ">":
            if not pila:
                return False
            ultimo_apertura = pila.pop()
        #Verificar que el paréntesis de cierre coincida con el último paréntesis de apertura
            if (ultimo_apertura == '(' and caracter != ')') or \
               (ultimo_apertura == '{' and caracter != '}') or \
               (ultimo_apertura == '[' and caracter != ']') or \
               (ultimo_apertura == '<' and caracter != '>'):
                return False
    #Al final si la pila esta vacia, significa que todos los parentesis de apertura tienen su correspondiente cierre
    return len(pila) == 0

#Solicitar al usuario que ingrese una expresión
expresion = input("Ingrese una expresión matematica: ")
#Llamar a la función verificar_parentesis con la expresión ingresada por el usuario y mostrar el resultado
resultado = verificar_parentesis(expresion)
#Mostrar el resultado al usuario
if resultado:
    print("Los simbolos de agrupacion están balanceados.")
else:
    print("Los simbolos de agrupacion no están balanceados.")

