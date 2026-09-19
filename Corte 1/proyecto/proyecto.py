import tkinter as tk
from Fractal_engine import FractalEngine

def iniciar_app():
    try:
        n = int(entry_nivel.get())
    except ValueError:
        n = 3

    motor.ejecutar_render(n)
    
    # Recibimos también el tiempo en milisegundos
    total, max_stack, tiempo = motor.obtener_auditoria()
    
    # Mostramos las llamadas, la pila máxima y el tiempo de ejecución en ms
    lbl_stats.config(text=f"Llamadas: {total} | Pila: {max_stack} | Tiempo: {tiempo:.2f} ms")

root = tk.Tk()
root.title("Auditoría de Memoria y Generador de Copo de Nieve a la -1")
root.geometry("900x1000")
root.configure(bg="#1e1e1e")

frame_top = tk.Frame(root, bg="#1e1e1e")
frame_top.pack(pady=10)

lbl_info = tk.Label(frame_top, text="Nivel (n):", fg="white", bg="#1e1e1e", font=("Arial", 11))
lbl_info.pack(side=tk.LEFT, padx=5)

entry_nivel = tk.Entry(frame_top, width=5, font=("Arial", 11))
entry_nivel.insert(0, "3")
entry_nivel.pack(side=tk.LEFT, padx=5)

btn_render = tk.Button(frame_top, text="Renderizar Fractal", command=iniciar_app, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
btn_render.pack(side=tk.LEFT, padx=10)

canvas_grafico = tk.Canvas(root, width=750, height=750, bg="black", highlightthickness=0)
canvas_grafico.pack(pady=10)

lbl_stats = tk.Label(root, text="Llamadas: 0 | Pila: 0 | Tiempo: 0.00 ms", fg="#00ff00", bg="#1e1e1e", font=("Consolas", 10))
lbl_stats.pack(pady=10)

motor = FractalEngine(canvas_grafico, 750, 750)
iniciar_app()

root.mainloop()