from AASTHO import Flexible_Pavement
import tkinter as tk

import tkinter as tk

def setTextLabel(Label, text):
    Label.config(text=text)

def setResult(confiabilidad, desviacion, structural_number, delta_psi, mr):
    try:
        # Convierte los valores ingresados a números flotantes
        confiabilidad = float(confiabilidad)
        desviacion = float(desviacion)
        structural_number = float(structural_number)
        delta_psi = float(delta_psi)
        mr = float(mr)

        # Realiza la operación matemática (puedes cambiar esto según tus necesidades)
        resultado = Flexible_Pavement(
            confiabilidad,
            desviacion,
            structural_number,
            delta_psi,
            mr
        )

        # Muestra el resultado en una window emergente
        resultado_label.config(text=f"Resultado: {resultado.getAxes()}")
    except ValueError:
        resultado_label.config(text="¡Ingresa valores numéricos válidos!")

# Crear una window
window = tk.Tk()
window.title("Calculadora de Confiabilidad")

# Etiquetas entrada
confiabilidad_label = tk.Label(window, text="Confiabilidad:")
desviacion_label = tk.Label(window, text="Desviación estándar:")
structural_number_label = tk.Label(window, text="Parámetro 1:")
delta_psi_label = tk.Label(window, text="Parámetro 2:")
mr_label = tk.Label(window, text="Parámetro 3:")

# Campos de entrada
confiabilidad_entry = tk.Entry(window)
desviacion_entry = tk.Entry(window)
structural_number_entry = tk.Entry(window)
delta_psi_entry = tk.Entry(window)
mr_entry = tk.Entry(window)

# Botón para realizar la operación
calcular_button = tk.Button(window, text="Calcular", command=lambda: setResult(
    confiabilidad_entry.get(),
    desviacion_entry.get(),
    structural_number_entry.get(),
    delta_psi_entry.get(),
    mr_entry.get()
))

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(window, text="Resultado:")

# Diseño de la interfaz
confiabilidad_label.grid(row=0, column=0)
desviacion_label.grid(row=1, column=0)
structural_number_label.grid(row=2, column=0)
delta_psi_label.grid(row=3, column=0)
mr_label.grid(row=4, column=0)

confiabilidad_entry.grid(row=0, column=1)
desviacion_entry.grid(row=1, column=1)
structural_number_entry.grid(row=2, column=1)
delta_psi_entry.grid(row=3, column=1)
mr_entry.grid(row=4, column=1)

calcular_button.grid(row=5, columnspan=2)
resultado_label.grid(row=6, columnspan=2)

# Iniciar la aplicación
window.mainloop()


