import gc
import tracemalloc

# -------------------------------------------------------------
# Definición de la clase Carro (necesaria para la Parte 1 y 3)
# -------------------------------------------------------------
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Iniciar el rastreo de memoria al comienzo de la ejecución
tracemalloc.start()

print("=== INICIO DE LA EJECUCIÓN ===")
actual, pico = tracemalloc.get_traced_memory()
print(f"Memoria inicial utilizada: {actual / 1024:.2f} KB\n")


# -------------------------------------------------------------
# PARTE 1: Asignación y liberación de memoria
# -------------------------------------------------------------
print("--- PARTE 1: Asignación y liberación de memoria ---")
carro1 = Carro("Toyota", "Corolla")
nombre = "Juan"
edad = 30
personas = ["Ana", "Luis", "Carlos"]

actual, _ = tracemalloc.get_traced_memory()
print(f"Uso de memoria despues de la declaracion: {actual / 1024:.2f} KB")

# Liberar las variables asignándoles None o usando del
carro1 = None
nombre = None
edad = None
personas = None

actual, _ = tracemalloc.get_traced_memory()
print(f"Uso de memoria luego de la eliminacion: {actual / 1024:.2f} KB\n")


# -------------------------------------------------------------
# PARTE 2: Variables y referencias
# -------------------------------------------------------------
print("--- PARTE 2: Variables y referencias ---")
nombre = "Maria"
edad = 25
# Creación de un arreglo (lista) grande de datos
personas = ["Ana", "Luis", "Carlos", "Pedro", "Sofia", "Marta", "Diego", "Lucia", "Javier", "Elena"]

# Asignación por referencia/etiqueta en Python
personas_ref = personas 
# Modificar el contenido a través de la nueva referencia
personas_ref = ["Ana", "Luis"]

actual, _ = tracemalloc.get_traced_memory()
print(f"Uso de memoria despues de las asignaciones y referencias: {actual / 1024:.2f} KB\n")


# -------------------------------------------------------------
# PARTE 3: Gestión de la basura (Garbage Collection)
# -------------------------------------------------------------
print("--- PARTE 3: Gestión de la basura (Garbage Collection) ---")
carros = []
for i in range(10000):
    carro = Carro(f"Marca{i}", f"Modelo{i}")
    carros.append(carro)

actual, _ = tracemalloc.get_traced_memory()
print(f"Uso de memoria despues de la creacion masiva de objetos: {actual / 1024:.2f} KB")

# Liberar el contenedor principal de objetos
del carros

# Forzar la ejecución del recolector de basura
gc.collect()

actual, pico = tracemalloc.get_traced_memory()
print(f"Uso de memoria luego de la recoleccion de basura: {actual / 1024:.2f} KB")
print(f"Pico máximo de memoria alcanzado durante todo el script: {pico / 1024:.2f} KB\n")

# Detener el rastreo de memoria al finalizar
tracemalloc.stop()
print("=== FIN DE LA EJECUCIÓN ===")