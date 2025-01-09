import tkinter as tk
from tkinter import ttk, messagebox
import math

# Clases de figuras importadas aquí
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio: int):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor: int):
        if valor <= 0:
            raise ValueError("El radio debe ser un número positivo")
        self._radio = valor

    def calcularArea(self) -> float:
        return math.pi * math.pow(self.radio, 2)

    def calcularPerimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @base.setter
    def base(self, valor: int):
        if valor <= 0:
            raise ValueError("La base debe ser un número positivo")
        self._base = valor

    @altura.setter
    def altura(self, valor: int):
        if valor <= 0:
            raise ValueError("La altura debe ser un número positivo")
        self._altura = valor

    def calcularArea(self) -> float:
        return self.base * self.altura

    def calcularPerimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, valor: int):
        if valor <= 0:
            raise ValueError("El lado debe ser un número positivo")
        self._lado = valor

    def calcularArea(self) -> float:
        return self.lado * self.lado

    def calcularPerimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @base.setter
    def base(self, valor: int):
        if valor <= 0:
            raise ValueError("La base debe ser un número positivo")
        self._base = valor

    @altura.setter
    def altura(self, valor: int):
        if valor <= 0:
            raise ValueError("La altura debe ser un número positivo")
        self._altura = valor

    def calcularArea(self) -> float:
        return (self.base * self.altura) / 2

    def calcularPerimetro(self) -> float:
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self) -> float:
        return math.sqrt(self.base**2 + self.altura**2)

# Función principal de la interfaz
def calcular_figura():
    figura_seleccionada = combo_figura.get()
    try:
        if figura_seleccionada == "Círculo":
            radio = int(entrada1.get())
            figura = Circulo(radio)
        elif figura_seleccionada == "Rectángulo":
            base = int(entrada1.get())
            altura = int(entrada2.get())
            figura = Rectangulo(base, altura)
        elif figura_seleccionada == "Cuadrado":
            lado = int(entrada1.get())
            figura = Cuadrado(lado)
        elif figura_seleccionada == "Triángulo Rectángulo":
            base = int(entrada1.get())
            altura = int(entrada2.get())
            figura = TrianguloRectangulo(base, altura)
        else:
            messagebox.showerror("Error", "Seleccione una figura válida")
            return

        area = figura.calcularArea()
        perimetro = figura.calcularPerimetro()
        messagebox.showinfo("Resultados", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

raiz = tk.Tk()
raiz.title("Calculadora de Figuras")

tk.Label(raiz, text="Seleccione una figura:").grid(row=0, column=0, padx=10, pady=5)

combo_figura = ttk.Combobox(raiz, values=["Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo"])
combo_figura.grid(row=0, column=1, padx=10, pady=5)
combo_figura.set("Seleccione")

tk.Label(raiz, text="Dato 1:").grid(row=1, column=0, padx=10, pady=5)
entrada1 = tk.Entry(raiz)
entrada1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(raiz, text="Dato 2 (si aplica):").grid(row=2, column=0, padx=10, pady=5)
entrada2 = tk.Entry(raiz)
entrada2.grid(row=2, column=1, padx=10, pady=5)

btn_calcular = tk.Button(raiz, text="Calcular", command=calcular_figura)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

raiz.mainloop()
