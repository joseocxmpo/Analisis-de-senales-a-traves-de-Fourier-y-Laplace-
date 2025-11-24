import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def generar_serie_fourier():
    t = np.linspace(-np.pi, np.pi, 2000, endpoint=False)
    square_wave = np.sign(np.sin(t))

    n_armonicos = 25  # solo impares
    serie = np.zeros_like(t, dtype=float)
    for k in range(1, 2 * n_armonicos, 2):
        serie += (4 / (np.pi * k)) * np.sin(k * t)

    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(t, square_wave, label="Onda cuadrada ideal", linewidth=2)
    ax.plot(t, serie, label=f"Aproximación Fourier (N={n_armonicos})", linestyle="--")
    ax.set_title("Serie de Fourier – onda cuadrada")
    ax.set_xlabel("Tiempo (rad)")
    ax.set_ylabel("Amplitud")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    explicacion = (
        "Concepto\n"
        "La serie de Fourier escribe una señal periódica como suma de senos y cosenos. "
        "Si la señal es impar, solo se conservan términos senoidales.\n\n"
        "Resultado\n"
        "Los armónicos impares determinan la onda cuadrada: el valor promedio y los coeficientes aₙ se anulan.\n\n"
        "Interpretación\n"
        "Al sumar más armónicos impares la serie se aproxima a la onda cuadrada ideal; "
        "los sobretiros en los saltos corresponden al fenómeno de Gibbs.\n\n"
        "f(t) = (4/π)·[sin(t) + sin(3t)/3 + sin(5t)/5 + …]\n"
        "a₀ = 0, aₙ = 0, bₙ = 4/(πn) para n impar y bₙ = 0 para n par."
    )
    return fig, explicacion


def generar_transformada_laplace():
    t = np.linspace(0, 3, 600)
    f_t = np.where(t < 1, 2 * t, 2)

    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(t, f_t, linewidth=2)
    ax.set_title("Función por partes – Laplace")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    explicacion = (
        "Concepto\n"
        "La transformada de Laplace lleva señales temporales al dominio complejo s "
        "para estudiar estabilidad y respuesta de sistemas LTI.\n\n"
        "Resultado\n"
        "La integral por tramos produce un factor exponencial que desplaza la contribución del segmento constante.\n\n"
        "Interpretación\n"
        "El término e^{-s} aparece por el cambio en t=1 y la ROC Re(s)>0 mantiene la integral convergente.\n\n"
        "f(t) = 2t para 0≤t<1 y f(t)=2 para t≥1;\n"
        "F(s) = (2/s²)·(1 - e^{-s}); ROC: Re(s) > 0."
    )
    return fig, explicacion


def render_plot(fig):
    global plot_canvas
    if plot_canvas is not None:
        plot_canvas.get_tk_widget().destroy()
    plot_canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    plot_canvas.draw()
    plot_canvas.get_tk_widget().pack(fill="both", expand=True)


def mostrar_ejercicio(nombre):
    if nombre == "Serie de Fourier de onda cuadrada":
        fig, texto = generar_serie_fourier()
    elif nombre == "Transformada de Laplace por partes":
        fig, texto = generar_transformada_laplace()
    else:
        return

    render_plot(fig)

    texto_box.config(state="normal")
    texto_box.delete("1.0", tk.END)
    texto_box.insert(tk.END, texto)
    texto_box.config(state="disabled")


def crear_gui(root):
    root.title("Análisis de Señales: Fourier y Laplace")
    root.geometry("960x520")

    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    menu_frame = ttk.Frame(root, padding=15)
    menu_frame.grid(row=0, column=0, sticky="ns")

    ttk.Label(menu_frame, text="Ejercicios", font=("Segoe UI", 12, "bold")).pack(pady=(0, 10))

    ttk.Button(
        menu_frame,
        text="Serie de Fourier de onda cuadrada",
        command=lambda: mostrar_ejercicio("Serie de Fourier de onda cuadrada"),
        width=28,
    ).pack(pady=5)

    ttk.Button(
        menu_frame,
        text="Transformada de Laplace por partes",
        command=lambda: mostrar_ejercicio("Transformada de Laplace por partes"),
        width=28,
    ).pack(pady=5)

    content_frame = ttk.Frame(root, padding=10)
    content_frame.grid(row=0, column=1, sticky="nsew")
    content_frame.columnconfigure(0, weight=1)
    content_frame.rowconfigure(0, weight=3)
    content_frame.rowconfigure(1, weight=2)

    global plot_frame
    plot_frame = ttk.LabelFrame(content_frame, text="Visualización")
    plot_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    global texto_box
    text_frame = ttk.LabelFrame(content_frame, text="Explicación y conceptos")
    text_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    texto_box = tk.Text(text_frame, wrap="word", font=("Segoe UI", 10))
    texto_box.pack(fill="both", expand=True)
    texto_box.config(state="disabled")

    mostrar_ejercicio("Serie de Fourier de onda cuadrada")


if __name__ == "__main__":
    root = tk.Tk()
    plot_canvas = None
    plot_frame = None
    texto_box = None
    crear_gui(root)
    root.mainloop()