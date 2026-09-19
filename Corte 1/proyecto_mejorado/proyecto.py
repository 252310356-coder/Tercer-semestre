import pygame
import threading
from Fractal_engine import FractalEngine

# Inicializar Pygame
pygame.init()
ANCHO, ALTO = 800, 850
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Motor Acelerado Pygame - Copo de Koch")

FUENTE = pygame.font.SysFont("Consolas", 16)
FUENTE_TITULO = pygame.font.SysFont("Arial", 18, bold=True)

motor = FractalEngine()

# Variables de estado globales
nivel_actual = 6
cargando = False
datos_metricas = {"llamadas": 0, "pila": 0, "tiempo": 0.0}
segmentos_cache = []

def ejecutar_en_segundo_plan(nivel):
    global cargando, segmentos_cache, datos_metricas
    cargando = True
    
    # Ejecutar cálculo pesado en hilo secundario
    motor.calcular_fractal(nivel, ANCHO, ALTO - 100)
    llamadas, pila, tiempo, segs = motor.obtener_auditoria()
    
    datos_metricas = {"llamadas": llamadas, "pila": pila, "tiempo": tiempo}
    segmentos_cache = segs
    cargando = False

# Lanzar hilo inicial
threading.Thread(target=ejecutar_en_segundo_plan, args=(nivel_actual,)).start()

# Bucle principal de la aplicación
reloj = pygame.time.Clock()
ejecutando = True
input_texto = str(nivel_actual)
activo_input = False

while ejecutando:
    pantalla.fill((30, 30, 30))  # Fondo oscuro

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Control simple de clic en caja de texto
            if 100 <= evento.pos[0] <= 150 and 15 <= evento.pos[1] <= 45:
                activo_input = True
            else:
                activo_input = False
                
        elif evento.type == pygame.KEYDOWN and activo_input:
            if evento.key == pygame.K_RETURN:
                try:
                    nuevo_n = int(input_texto)
                    if 0 <= nuevo_n <= 11:  # Permite romper el límite hasta 11 con seguridad
                        nivel_actual = nuevo_n
                        if not cargando:
                            threading.Thread(target=ejecutar_en_segundo_plan, args=(nivel_actual,)).start()
                except ValueError:
                    pass
            elif evento.key == pygame.K_BACKSPACE:
                input_texto = input_texto[:-1]
            else:
                if evento.unicode.isdigit() and len(input_texto) < 2:
                    input_texto += evento.unicode

    # --- RENDERIZADO GRÁFICO (Área del Fractal) ---
    area_dibujo = pygame.Rect(0, 100, ANCHO, ALTO - 100)
    pygame.draw.rect(pantalla, (15, 15, 15), area_dibujo)

    # Dibujar todos los segmentos cacheados con Pygame (Acelerado por GPU/CPU)
    for seg in segmentos_cache:
        pygame.draw.aaline(pantalla, (0, 255, 255), (seg[0], seg[1]), (seg[2], seg[3]))

    # --- PANEL DE CONTROL SUPERIOR ---
    pygame.draw.rect(pantalla, (45, 45, 45), (0, 0, ANCHO, 100))
    
    # Texto de Nivel
    txt_lbl = FUENTE_TITULO.render("Nivel (n):", True, (255, 255, 255))
    pantalla.blit(txt_lbl, (20, 18))

    # Caja de texto
    color_caja = (0, 122, 204) if activo_input else (80, 80, 80)
    pygame.draw.rect(pantalla, color_caja, (100, 15, 50, 30), border_radius=4)
    txt_input = FUENTE.render(input_texto, True, (255, 255, 255))
    pantalla.blit(txt_input, (112, 20))

    # Botón de ayuda informativa
    btn_info = FUENTE.render("Presiona ENTER para actualizar", True, (180, 180, 180))
    pantalla.blit(btn_info, (170, 20))

    # Indicador de estado (Cargando vs Listo)
    if cargando:
        txt_estado = FUENTE_TITULO.render("PROCESANDO EN SEGUNDO PLANO...", True, (255, 165, 0))
    else:
        txt_estado = FUENTE_TITULO.render("ESTADO: LISTO", True, (0, 255, 0))
    pantalla.blit(txt_estado, (480, 18))

    # Panel inferior de Métricas de Auditoría
    metrics_str = f"Llamadas: {datos_metricas['llamadas']} | Pila: {datos_metricas['pila']} | Tiempo: {datos_metricas['tiempo']:.2f} ms"
    txt_metrics = FUENTE.render(metrics_str, True, (0, 255, 0))
    pantalla.blit(txt_metrics, (20, 65))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()