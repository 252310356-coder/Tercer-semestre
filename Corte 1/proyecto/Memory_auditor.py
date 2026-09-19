class MemoryAuditor:
    def __init__(self):
        self.total_llamadas = 0
        self.max_profundidad_stack = 0

    def registrar_llamada(self, profundidad_actual):
        self.total_llamadas += 1
        if profundidad_actual > self.max_profundidad_stack:
            self.max_profundidad_stack = profundidad_actual

    def reiniciar(self):
        self.total_llamadas = 0
        self.max_profundidad_stack = 0

    def get_total_llamadas(self):
        return self.total_llamadas

    def get_max_profundidad(self):
        return self.max_profundidad_stack