import math
import time
from Memory_auditor import MemoryAuditor

class FractalEngine:
    """
    Motor encargado de calcular y renderizar el fractal del Copo de Nieve de Koch,
    además de auditar el uso de memoria (pila y llamadas) y el tiempo de ejecución.
    """
    
    def __init__(self, canvas_tk, ancho, alto):
        # Inicializa los atributos principales del motor con el canvas de Tkinter y sus dimensiones
        self.canvas_tk = canvas_tk
        self.ancho = ancho
        self.alto = alto
        self.auditor = MemoryAuditor()  # Instancia el objeto que audita la recursión
        self.tiempo_ms = 0.0  # Variable para almacenar el tiempo total medido en milisegundos

    def _copo_koch(self, x0, y0, x1, y1, nivel, profundidad_actual):
        """
        Función recursiva que divide una línea en 4 partes aplicando la geometría de Koch.
        """
        # Registra en el auditor una llamada más y la profundidad actual de la pila (stack)
        self.auditor.registrar_llamada(profundidad_actual)

        # CASO BASE: Si el nivel de recursión llega a 0, se detiene la división y se dibuja la línea final
        if nivel == 0:
            self.canvas_tk.create_line(x0, y0, x1, y1, fill="cyan", width=1.5)
            return

        # Calcula la longitud total del segmento en los ejes X e Y
        dx = x1 - x0
        dy = y1 - y0

        # Calcula el primer punto de corte (a 1/3 de la línea original)
        p1_x = x0 + dx / 3.0
        p1_y = y0 + dy / 3.0

        # Calcula el segundo punto de corte (a 2/3 de la línea original)
        p2_x = x0 + 2.0 * dx / 3.0
        p2_y = y0 + 2.0 * dy / 3.0

        # Define el ángulo de rotación de 60 grados (pi / 3 radianes) para levantar el pico
        angulo = math.pi / 3.0  # 60 grados
        cos_a = math.cos(angulo)
        sin_a = math.sin(angulo)

        # Obtiene el vector direccion del segmento intermedio entre p1 y p2
        vx = p2_x - p1_x
        vy = p2_y - p1_y
        
        # Aplica matrices de rotación trigonométrica para calcular las coordenadas exactas del pico superior
        pico_x = p1_x + (vx * cos_a - vy * sin_a)
        pico_y = p1_y + (vx * sin_a + vy * cos_a)

        # LLAMADAS RECURSIVAS: Divide la línea original en 4 nuevos subsegmentos (nivel - 1)
        # 1. Del inicio (x0, y0) al primer tercio (p1_x, p1_y)
        self._copo_koch(x0, y0, p1_x, p1_y, nivel - 1, profundidad_actual + 1)
        
        # 2. Del primer tercio (p1_x, p1_y) hasta el pico exterior (pico_x, pico_y)
        self._copo_koch(p1_x, p1_y, pico_x, pico_y, nivel - 1, profundidad_actual + 1)
        
        # 3. Del pico (pico_x, pico_y) de bajada al segundo tercio (p2_x, p2_y)
        self._copo_koch(pico_x, pico_y, p2_x, p2_y, nivel - 1, profundidad_actual + 1)
        
        # 4. Del segundo tercio (p2_x, p2_y) hasta el final de la línea original (x1, y1)
        self._copo_koch(p2_x, p2_y, x1, y1, nivel - 1, profundidad_actual + 1)

    def ejecutar_render(self, nivel_maximo):
        """
        Prepara el entorno, calcula el triángulo inicial y mide el rendimiento del renderizado.
        """
        # Reinicia los contadores del auditor de memoria para una nueva ejecución
        self.auditor.reiniciar()
        
        # Limpia todos los trazos anteriores dibujados en el Canvas de Tkinter
        self.canvas_tk.delete("all")

        # Inicia el cronómetro de alta precisión para medir el tiempo exacto de procesamiento
        t_inicio = time.perf_counter()

        # Calcula el centro del lienzo (Canvas)
        cx, cy = self.ancho / 2, self.alto / 2
        
        # Calcula el radio óptimo del copo de nieve en función del tamaño del canvas
        radio = min(self.ancho, self.alto) * 0.46

        # Calcula matemáticamente mediante trigonometría los 3 vértices del triángulo equilátero base
        puntos = []
        for i in range(3):
            angulo = i * (2 * math.pi / 3) - math.pi / 2
            px = cx + radio * math.cos(angulo)  # Coordenada X del vértice
            py = cy + radio * math.sin(angulo)  # Coordenada Y del vértice
            puntos.append((px, py))

        # Dispara la recursión inicial conectando los 3 lados del triángulo madre:
        # Lado 1: Del vértice 0 al vértice 1
        self._copo_koch(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1], nivel_maximo, 1)
        
        # Lado 2: Del vértice 1 al vértice 2
        self._copo_koch(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1], nivel_maximo, 1)
        
        # Lado 3: Del vértice 2 de regreso al vértice 0 (cierra el triángulo)
        self._copo_koch(puntos[2][0], puntos[2][1], puntos[0][0], puntos[0][1], nivel_maximo, 1)

        # Detiene el cronómetro de alta precisión al finalizar el renderizado
        t_fin = time.perf_counter()
        
        # Calcula el tiempo total transcurrido y lo convierte a milisegundos
        self.tiempo_ms = (t_fin - t_inicio) * 1000.0

    def obtener_auditoria(self):
        """
        Devuelve las métricas recopiladas por el motor tras el renderizado.
        """
        return self.auditor.get_total_llamadas(), self.auditor.get_max_profundidad(), self.tiempo_ms