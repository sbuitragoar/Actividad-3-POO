import tkinter as tk
from tkinter import messagebox


class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            return f"{self.nombre} debe recibir un salario mensual de ${int(salario_mensual)}."
        else:
            return f"{self.nombre} recibe un salario mensual menor o igual a $450,000."


def calcular_salario():
    try:
        nombre = entrada_nombre.get()
        salario_por_hora = int(entrada_salario_por_hora.get())
        horas_trabajadas = int(entrada_horas_trabajadas.get())

        empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
        resultado = empleado.mostrar_informacion()
        messagebox.showinfo("Información del Empleado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


raiz = tk.Tk()
raiz.title("Calculadora de Salario Mensual")

tk.Label(raiz, text="Nombre del Empleado:").grid(row=0, column=0, padx=10, pady=5)
entrada_nombre = tk.Entry(raiz)
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(raiz, text="Salario por Hora ($):").grid(row=1, column=0, padx=10, pady=5)
entrada_salario_por_hora = tk.Entry(raiz)
entrada_salario_por_hora.grid(row=1, column=1, padx=10, pady=5)

tk.Label(raiz, text="Horas Trabajadas en el Mes:").grid(row=2, column=0, padx=10, pady=5)
entrada_horas_trabajadas = tk.Entry(raiz)
entrada_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

tk.Button(raiz, text="Calcular Salario", command=calcular_salario).grid(row=3, column=0, columnspan=2, pady=10)

raiz.mainloop()
