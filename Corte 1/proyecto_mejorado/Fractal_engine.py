import math
import time
from Memory_auditor import MemoryAuditor

class FractalEngine:
    def __init__(self):
        self.auditor = MemoryAuditor()
        self.tiempo_ms = 0.0
        self.segmentos = []  # Almacenará todas las coordenadas (x0, y0, x1, y1)

    def _copo_koch(self, x0, y0, x1, y1, nivel, profundidad_actual):
        self.auditor.registrar_llamada(profundidad_actual)

        if nivel == 0:
            self.segmentos.append((x0, y0, x1, y1))
            return

        dx = x1 - x0
        dy = y1 - y0

        p1_x = x0 + dx / 3.0
        p1_y = y0 + dy / 3.0

        p2_x = x0 + 2.0 * dx / 3.0
        p2_y = y0 + 2.0 * dy / 3.0

        angulo = math.pi / 3.0
        cos_a = math.cos(angulo)
        sin_a = math.sin(angulo)

        vx = p2_x - p1_x
        vy = p2_y - p1_y
        pico_x = p1_x + (vx * cos_a - vy * sin_a)
        pico_y = p1_y + (vx * sin_a + vy * cos_a)

        self._copo_koch(x0, y0, p1_x, p1_y, nivel - 1, profundidad_actual + 1)
        self._copo_koch(p1_x, p1_y, pico_x, pico_y, nivel - 1, profundidad_actual + 1)
        self._copo_koch(pico_x, pico_y, p2_x, p2_y, nivel - 1, profundidad_actual + 1)
        self._copo_koch(p2_x, p2_y, x1, y1, nivel - 1, profundidad_actual + 1)

    def calcular_fractal(self, nivel_maximo, ancho, alto):
        self.auditor.reiniciar()
        self.segmentos = []

        t_inicio = time.perf_counter()

        cx, cy = ancho / 2, alto / 2 + 50
        radio = min(ancho, alto) * 0.42

        puntos = []
        for i in range(3):
            angulo = i * (2 * math.pi / 3) - math.pi / 2
            px = cx + radio * math.cos(angulo)
            py = cy + radio * math.sin(angulo)
            puntos.append((px, py))

        self._copo_koch(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1], nivel_maximo, 1)
        self._copo_koch(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1], nivel_maximo, 1)
        self._copo_koch(puntos[2][0], puntos[2][1], puntos[0][0], puntos[0][1], nivel_maximo, 1)

        t_fin = time.perf_counter()
        self.tiempo_ms = (t_fin - t_inicio) * 1000.0

    def obtener_auditoria(self):
        return self.auditor.get_total_llamadas(), self.auditor.get_max_profundidad(), self.tiempo_ms, self.segmentos