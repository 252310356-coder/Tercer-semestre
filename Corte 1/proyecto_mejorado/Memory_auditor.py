class MemoryAuditor:
    def __init__(self):
        self.total_llamadas = 0
        self.max_profundidad = 0

    def reiniciar(self):
        self.total_llamadas = 0
        self.max_profundidad = 0

    def registrar_llamada(self, profundidad_actual):
        self.total_llamadas += 1
        if profundidad_actual > self.max_profundidad:
            self.max_profundidad = profundidad_actual

    def get_total_llamadas(self):
        return self.total_llamadas

    def get_max_profundidad(self):
        return self.max_profundidad