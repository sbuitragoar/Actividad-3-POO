import tkinter as tk
from tkinter import messagebox


class Jerarquia_Numeros:
    @staticmethod
    def clasificar_numeros(numero_A, numero_B):
        if numero_A > numero_B:
            return f"El número {numero_A} es mayor que {numero_B}."
        elif numero_A == numero_B:
            return f"El número {numero_A} es igual a {numero_B}."
        else:
            return f"El número {numero_A} es menor que {numero_B}."


def clasificar():
    try:
        numero_A = int(entrada_numero_A.get())
        numero_B = int(entrada_numero_B.get())
        resultado = Jerarquia_Numeros.clasificar_numeros(numero_A, numero_B)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


raiz = tk.Tk()
raiz.title("Clasificador de Números")

tk.Label(raiz, text="Ingrese el número 1:").grid(row=0, column=0, padx=10, pady=5)
entrada_numero_A = tk.Entry(raiz)
entrada_numero_A.grid(row=0, column=1, padx=10, pady=5)

tk.Label(raiz, text="Ingrese el número 2:").grid(row=1, column=0, padx=10, pady=5)
entrada_numero_B = tk.Entry(raiz)
entrada_numero_B.grid(row=1, column=1, padx=10, pady=5)

tk.Button(raiz, text="Clasificar", command=clasificar).grid(row=2, column=0, columnspan=2, pady=10)

raiz.mainloop()
