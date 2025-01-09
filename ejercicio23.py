import math
import tkinter as tk
from tkinter import messagebox


class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_raices(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return round(raiz1, 2), round(raiz2, 2)
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return round(raiz, 2),
        else:
            return None


def calcular():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        ecuacion = EcuacionSegundoGrado(a, b, c)
        soluciones = ecuacion.calcular_raices()

        if soluciones:
            resultado = f"Las soluciones son: {soluciones}"
        else:
            resultado = "La ecuación no tiene soluciones reales."

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


raiz = tk.Tk()
raiz.title("Calculadora de Ecuaciones de Segundo Grado")

tk.Label(raiz, text="Coeficiente A:").grid(row=0, column=0, padx=10, pady=5)
entrada_a = tk.Entry(raiz)
entrada_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(raiz, text="Coeficiente B:").grid(row=1, column=0, padx=10, pady=5)
entrada_b = tk.Entry(raiz)
entrada_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(raiz, text="Coeficiente C:").grid(row=2, column=0, padx=10, pady=5)
entrada_c = tk.Entry(raiz)
entrada_c.grid(row=2, column=1, padx=10, pady=5)

tk.Button(raiz, text="Calcular Raíces", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

raiz.mainloop()
