import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, codigo, nombres, horas_mes, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_mes = horas_mes
        self.valor_hora = valor_hora
        self.retencion = retencion
        self.salario_bruto = 0
        self.salario_neto = 0

    def salarios(self):
        self.salario_bruto = self.horas_mes * self.valor_hora
        self.salario_neto = int(self.salario_bruto - self.salario_bruto * (self.retencion / 100))

    def mostrar_resultados(self):
        self.salarios()
        return (f"Código: {self.codigo}\n"
                f"Nombres: {self.nombres}\n"
                f"Salario Bruto: {self.salario_bruto}\n"
                f"Salario Neto: {self.salario_neto}")


def calcular_salario():
    try:
        codigo = codigo_entrada.get()
        nombres = nombres_entrada.get()
        horas_mes = int(horas_mes_entrada.get())
        valor_hora = int(valor_hora_entrada.get())
        retencion = float(retencion_entry.get())

        empleado = Empleado(codigo, nombres, horas_mes, valor_hora, retencion)
        resultados = empleado.mostrar_resultados()
        messagebox.showinfo("Resultados", resultados)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")


root = tk.Tk()
root.title("Calculadora de Salarios")

tk.Label(root, text="Código:").grid(row=0, column=0, padx=10, pady=5)
codigo_entrada = tk.Entry(root)
codigo_entrada.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
nombres_entrada = tk.Entry(root)
nombres_entrada.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Horas trabajadas al mes:").grid(row=2, column=0, padx=10, pady=5)
horas_mes_entrada = tk.Entry(root)
horas_mes_entrada.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Valor por hora:").grid(row=3, column=0, padx=10, pady=5)
valor_hora_entrada = tk.Entry(root)
valor_hora_entrada.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Retención en la fuente (%):").grid(row=4, column=0, padx=10, pady=5)
retencion_entry = tk.Entry(root)
retencion_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Calcular Salario", command=calcular_salario).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
