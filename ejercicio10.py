import tkinter as tk
from tkinter import messagebox


class Estudiante:
    # Atributos de clase
    numeros_inscritos = 0
    pago_matricula_base = 50000

    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        self.pago_mat = 0
        Estudiante.registro()

    def pago_matricula(self):
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            self.pago_mat = int(Estudiante.pago_matricula_base + 0.03 * self.patrimonio)
        else:
            self.pago_mat = Estudiante.pago_matricula_base
        return f"Estudiante {self.nombres} (Inscripción: {self.numero_inscripcion}) debe pagar ${self.pago_mat}"

    @classmethod
    def registro(cls):
        cls.numeros_inscritos += 1


def registrar_estudiante():
    try:
        numero_inscripcion = entrada_numero_inscripcion.get()
        nombres = entrada_nombres.get()
        patrimonio = int(entrada_patrimonio.get())
        estrato_social = int(entrada_estrato_social.get())

        estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato_social)
        resultado = estudiante.pago_matricula()
        messagebox.showinfo("Matrícula Calculada", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para todos los campos.")


raiz = tk.Tk()
raiz.title("Registro de Estudiantes")

tk.Label(raiz, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=5)
entrada_numero_inscripcion = tk.Entry(raiz)
entrada_numero_inscripcion.grid(row=0, column=1, padx=10, pady=5)

tk.Label(raiz, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
entrada_nombres = tk.Entry(raiz)
entrada_nombres.grid(row=1, column=1, padx=10, pady=5)

tk.Label(raiz, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
entrada_patrimonio = tk.Entry(raiz)
entrada_patrimonio.grid(row=2, column=1, padx=10, pady=5)

tk.Label(raiz, text="Estrato Social:").grid(row=3, column=0, padx=10, pady=5)
entrada_estrato_social = tk.Entry(raiz)
entrada_estrato_social.grid(row=3, column=1, padx=10, pady=5)

tk.Button(raiz, text="Registrar y Calcular Matrícula", command=registrar_estudiante).grid(row=4, column=0, columnspan=2, pady=10)

raiz.mainloop()
