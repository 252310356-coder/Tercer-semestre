import tkinter as tk
from Fractal_engine import FractalEngine

def iniciar_app():
    try:
        n = int(entry_nivel.get())
    except ValueError:
        n = 3

    # Desactivar botón durante la animación para evitar conflictos
    btn_render.config(state=tk.DISABLED)
    
    # Iniciar renderizado animado
    motor.ejecutar_render_animado(n, actualizar_interfaz_fin)

def actualizar_interfaz_fin():
    # Reactivar botón y actualizar estadísticas finales
    btn_render.config(state=tk.NORMAL)
    total, max_stack, tiempo = motor.obtener_auditoria()
    lbl_stats.config(text=f"Llamadas: {total} | Pila: {max_stack} | Tiempo: {tiempo:.2f} ms")

root = tk.Tk()
root.title("Paso a Paso: Generador y Auditor del Copo de Nieve")
root.geometry("600x740")
root.configure(bg="#1e1e1e")

frame_top = tk.Frame(root, bg="#1e1e1e")
frame_top.pack(pady=10)

lbl_info = tk.Label(frame_top, text="Nivel (n):", fg="white", bg="#1e1e1e", font=("Arial", 11))
lbl_info.pack(side=tk.LEFT, padx=5)

entry_nivel = tk.Entry(frame_top, width=5, font=("Arial", 11))
entry_nivel.insert(0, "2")  # Nivel 2 es ideal para ver los hexágonos paso a paso
entry_nivel.pack(side=tk.LEFT, padx=5)

btn_render = tk.Button(frame_top, text="Renderizar Paso a Paso", command=iniciar_app, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
btn_render.pack(side=tk.LEFT, padx=10)

canvas_grafico = tk.Canvas(root, width=500, height=500, bg="black", highlightthickness=0)
canvas_grafico.pack(pady=10)

lbl_stats = tk.Label(root, text="Llamadas: 0 | Pila: 0 | Tiempo: 0.00 ms", fg="#00ff00", bg="#1e1e1e", font=("Consolas", 10))
lbl_stats.pack(pady=10)

motor = FractalEngine(canvas_grafico, root, 500, 500)
iniciar_app()

root.mainloop()