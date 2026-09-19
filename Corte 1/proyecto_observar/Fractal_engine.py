import math
import time
from Memory_auditor import MemoryAuditor

class FractalEngine:
    def __init__(self, canvas_tk, root_tk, ancho, alto):
        self.canvas_tk = canvas_tk
        self.root_tk = root_tk
        self.ancho = ancho
        self.alto = alto
        self.auditor = MemoryAuditor()
        self.tiempo_ms = 0.0
        self.cola_pasos = []
        self.callback_fin = None
        self.t_inicio = 0.0

    def _generar_lista_koch(self, x0, y0, x1, y1, nivel, profundidad_actual):
        self.auditor.registrar_llamada(profundidad_actual)

        if nivel == 0:
            # Guardamos la línea final y sus puntos de inicio/fin para mostrarlos
            self.cola_pasos.append((x0, y0, x1, y1))
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

        self._generar_lista_koch(x0, y0, p1_x, p1_y, nivel - 1, profundidad_actual + 1)
        self._generar_lista_koch(p1_x, p1_y, pico_x, pico_y, nivel - 1, profundidad_actual + 1)
        self._generar_lista_koch(pico_x, pico_y, p2_x, p2_y, nivel - 1, profundidad_actual + 1)
        self._generar_lista_koch(p2_x, p2_y, x1, y1, nivel - 1, profundidad_actual + 1)

    def ejecutar_render_animado(self, nivel_maximo, callback_fin):
        self.auditor.reiniciar()
        self.canvas_tk.delete("all")
        self.cola_pasos = []
        self.callback_fin = callback_fin

        self.t_inicio = time.perf_counter()

        cx, cy = self.ancho / 2, self.alto / 2
        radio = min(self.ancho, self.alto) * 0.46

        puntos = []
        for i in range(3):
            angulo = i * (2 * math.pi / 3) - math.pi / 2
            px = cx + radio * math.cos(angulo)
            py = cy + radio * math.sin(angulo)
            puntos.append((px, py))

        # Generar recursivamente todos los trazos base del nivel seleccionado
        self._generar_lista_koch(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1], nivel_maximo, 1)
        self._generar_lista_koch(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1], nivel_maximo, 1)
        self._generar_lista_koch(puntos[2][0], puntos[2][1], puntos[0][0], puntos[0][1], nivel_maximo, 1)

        # Iniciar el bucle de animación visual paso a paso (velocidad en ms por lote de líneas)
        self._procesar_siguiente_paso()

    def _procesar_siguiente_paso(self):
        if not self.cola_pasos:
            # Terminó la animación
            t_fin = time.perf_counter()
            self.tiempo_ms = (t_fin - self.t_inicio) * 1000.0
            if self.callback_fin:
                self.callback_fin()
            return

        # Dibujamos en lotes pequeños (o de a 1 línea) para ver el flujo paso a paso
        # Ajusta el número '1' si quieres que pinte más rápido o más lento
        lotes = min(1, len(self.cola_pasos))
        
        for _ in range(lotes):
            x0, y0, x1, y1 = self.cola_pasos.pop(0)
            
            # 1. Dibujar la línea principal del segmento en cian
            self.canvas_tk.create_line(x0, y0, x1, y1, fill="cyan", width=1.5)
            
            # 2. Dibujar los puntos extremos (puntos de partida y fin) en color amarillo/rojo brillante
            # Esto cumple con mostrar de dónde parten y terminan las líneas
            radio_punto = 2
            self.canvas_tk.create_oval(x0 - radio_punto, y0 - radio_punto, x0 + radio_punto, y0 + radio_punto, fill="yellow", outline="")
            self.canvas_tk.create_oval(x1 - radio_punto, y1 - radio_punto, x1 + radio_punto, y1 + radio_punto, fill="red", outline="")

        # Velocidad de la animación en milisegundos (cambia a 10 o 50 para acelerar/desacelerar)
        self.root_tk.after(50, self._procesar_siguiente_paso)

    def obtener_auditoria(self):
        return self.auditor.get_total_llamadas(), self.auditor.get_max_profundidad(), self.tiempo_ms