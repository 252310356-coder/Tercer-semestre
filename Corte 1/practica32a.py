#Crear dos colas tipos queue, una para sumar
#los elementos de la cola y la otra para
#multiplicar
from queue import Queue
import random
cola1=Queue() # cola para sumar enteros
cola2=Queue() # cola para multiplicar float
#llenar las colas con elementos
suma= 0
multiplicacion= 1
historial1=[]
historial2=[]
for i in range(1,11):
    cola1.put(random.randint(1,10)) # enteros aleatorios entre 1 y 10
    cola2.put(random.uniform(1,10)) # float aleatorios entre 1 y 10
    historial1=historial1 + [cola1.queue[-1]] if not cola1.empty() else historial1 # historial de elementos de la cola1
    historial2=historial2 + [cola2.queue[-1]] if not cola2.empty() else historial2 # historial de elementos de la cola2
    suma= suma + cola1.get() # sumar elementos de la cola1
    multiplicacion= multiplicacion * cola2.get() # multiplicar elementos de la cola2


print("Elementos de la cola1: ", historial1)
print("Elementos de la cola2: ", historial2)

print ("Cantidad de elementos de la cola1: ", len(historial1))
print ("Cantidad de elementos de la cola2: ", len(historial2))

print("La suma de los elementos de la cola1 es: ", suma)
print("La multiplicación de los elementos de la cola2 es: ", multiplicacion)