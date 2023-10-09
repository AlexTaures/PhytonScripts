# import tkinter as tk
#
# # Definir una clase de estilo para los widgets
# class Estilos:
#     def __init__(self, ventana):
#         self.ventana = ventana
#         self.ventana.title("Generador de keys")
#         self.estilo_etiqueta = {'bg': 'lightblue', 'fg': 'black', 'font': ('Arial', 14)}
#         self.estilo_boton = {'bg': 'gray', 'fg': 'white', 'font': ('Arial', 12), 'relief': 'solid', 'bd': 1, "highlightbackground":"black"}
#
#     # Crear y mostrar los widgets con estilo
#     def mostrar_widgets(self):
#         entrada = tk.Entry(self.ventana)
#         entrada.pack(pady=10)
#
#         etiqueta = tk.Label(self.ventana, text="Ingrese la url del sitio", **self.estilo_etiqueta)
#         etiqueta.pack(pady=20)
#
#         boton = tk.Button(self.ventana, text="Botón con Estilo", **self.estilo_boton)
#         boton.pack(padx=20, pady=10)
#
# # Crear la ventana principal
# root = tk.Tk()
#
# # Crear una instancia de la clase de estilo y mostrar los widgets
# estilos = Estilos(root)
# estilos.mostrar_widgets()
#
# # Iniciar el bucle principal
# root.mainloop()

#################################
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Función para generar la clave a partir de la URL ingresada
def generar_keys():
    url = entrada.get()
    url = url.replace("https://sis-", "").replace(".salud.gob.sv/", "").replace("http://sis-", "").replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0')
    # Mostrar la clave en la etiqueta
    clave1.config(text=url)
    # Copiar la clave al portapapeles
    copiar_al_portapapeles(url)

# Función para copiar el texto al portapapeles
def copiar_al_portapapeles(texto):
    pyperclip.copy(texto)
    messagebox.showinfo("Clave en portapapeles", "¡La clave se copió con éxito!")

# Función para cerrar la aplicación
def cerrar():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de keys")

# Etiqueta 1 en la fila 0, columna 0
etiqueta1 = tk.Label(root, text="Ingresa la URL")
etiqueta1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Campo de entrada en la fila 1, columna 0
entrada = tk.Entry(root)
entrada.grid(row=1, column=0, padx=5, pady=5)

# Botón en la fila 1, columna 1
boton = tk.Button(root, text="Generar", command=generar_keys)
boton.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta para mostrar la clave generada
clave1 = tk.Label(root, text="", font=("Arial", 14))
clave1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Botón para copiar la clave al portapapeles
btnCopiar = tk.Button(root, text="Copiar", command=copiar_al_portapapeles)
btnCopiar.grid(row=3, column=0, columnspan=2, pady=10)

# Botón para cerrar la aplicación
btnCerrar = tk.Button(root, text="Cerrar", command=cerrar)
btnCerrar.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal
root.mainloop()
