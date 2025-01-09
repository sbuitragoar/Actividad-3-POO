import tkinter as tk
from tkinter import messagebox
import math


class Triangulo_Equilatero:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 3

    def altura(self):
        return round(self.lado * math.sqrt(3) / 2, 1)

    def area(self):
        return round((self.lado ** 2) * math.sqrt(3) / 4, 1)

    def mostrar_caracteristicas(self):
        return (f"Perímetro: {self.perimetro()} cm\n"
                f"Altura: {self.altura()} cm\n"
                f"Área: {self.area()} cm²")


def calcular():
    try:
        lado = float(entrada_lado.get())
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        triangulo = Triangulo_Equilatero(lado)
        resultados = triangulo.mostrar_caracteristicas()
        messagebox.showinfo("Características del Triángulo", resultados)
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")


raiz = tk.Tk()
raiz.title("Calculadora de Triángulo Equilátero")

tk.Label(raiz, text="Ingrese el tamaño del lado (cm):").pack(pady=10)
entrada_lado = tk.Entry(raiz)
entrada_lado.pack(pady=5)

tk.Button(raiz, text="Calcular", command=calcular).pack(pady=10)

raiz.mainloop()
