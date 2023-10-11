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
import pyperclip

# Función para generar la clave a partir de la URL ingresada
def generar_keys():
    url = urlInput.get()
    if url != '':
        sshUrl = url.replace("https://", "").replace("http://", "").replace('/','')
        str = sshUrl.replace('sis-', '').replace('siap-', '').replace('.salud.gob.sv','').replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('/','')

        keyText1.config(text = 's1s'+str+'-s14p')
        keyText2.config(text = 's14p'+str+'-s14p')
        sshText.config(text = 'ssh siap@' + sshUrl)
        btnCopiar1.config(state=tk.NORMAL)
        btnCopiar2.config(state=tk.NORMAL)
        btnSSH.config(state=tk.NORMAL)
    else:
        btnCopiar1.config(state=tk.DISABLED)
        btnCopiar2.config(state=tk.DISABLED)
        btnSSH.config(state=tk.DISABLED)


# Función para copiar el texto al portapapeles
def copiarClave(valor):
    if valor == 1:
        clave = keyText1.cget('text')
        btnCopiar1.config(state=tk.DISABLED)
    elif valor == 2:
        clave = keyText2.cget('text')
        btnCopiar2.config(state=tk.DISABLED)
    elif valor == 3:
        clave = sshText.cget('text')
        btnSSH.config(state=tk.DISABLED)
    else:
        clave = ""  # Definir un valor por defecto si valor no coincide con 1, 2 o 3

    pyperclip.copy(clave)

# Función para cerrar la aplicación
def cerrar():
    root.destroy()

#valores generales
anchokey = 40
bgBoton = 'sky blue'
fgBoton = 'dodger blue'
bgApp = 'dodger blue'
fgText = 'snow'

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de keys")
root.configure(bg=bgApp)

# Etiqueta 1 en la fila 0, columna 0
etiqueta1 = tk.Label(root, text="Ingresa la URL", bg=bgApp, fg=fgText,font=("Arial", 12, "bold"))
etiqueta1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Campo de entrada en la fila 1, columna 0
urlInput = tk.Entry(root, width = anchokey)
urlInput.grid(row=1, column=0, padx=5, pady=5)

# Botón en la fila 1, columna 1
botonGenerar = tk.Button(root, text="Generar", command=generar_keys, bg='midnight blue', fg=fgText)
botonGenerar.grid(row=1, column=1, padx=5, pady=5)

#clave 1
keyText1 = tk.Label(root, text="clave 1", font=("Arial", 9), width = anchokey, anchor="sw", bg=bgApp, fg=fgText)
keyText1.grid(row=2, column=0, padx=5, pady=5)
btnCopiar1 = tk.Button(root, text="Copiar", command=lambda:copiarClave(1), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold"))
btnCopiar1.grid(row=2, column=1, padx=5, pady=5)
btnCopiar1.config(state=tk.DISABLED)

#clave 2
keyText2 = tk.Label(root, text="clave 2", font=("Arial", 9), width = anchokey, anchor="sw", bg=bgApp, fg=fgText)
keyText2.grid(row=3, column=0, padx=0, pady=5)
btnCopiar2 = tk.Button(root, text="Copiar", command=lambda:copiarClave(2), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold"))
btnCopiar2.grid(row=3, column=1, padx=5, pady=5)
btnCopiar2.config(state=tk.DISABLED)

#SSH
sshText = tk.Label(root, text="ssh", font=("Arial", 9), width = anchokey, anchor="sw", bg=bgApp, fg=fgText)
sshText.grid(row=4, column=0, padx=5, pady=5)
btnSSH = tk.Button(root, text="Copiar", command=lambda:copiarClave(3), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold")    )
btnSSH.grid(row=4, column=1, padx=5, pady=5)
btnSSH.config(state=tk.DISABLED)


# Botón para cerrar la aplicación
btnCerrar = tk.Button(root, text="Cerrar", command=cerrar)
btnCerrar.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal
root.mainloop()
