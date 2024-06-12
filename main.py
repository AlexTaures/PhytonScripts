#################################
import tkinter as tk
import pyperclip
import csv

keys_file = '/home/alexander/Escritorio/Python/PhytonScripts/siapKeys.csv'

# Función para generar la clave a partir de la URL ingresada
def generar_keys():
    url = urlInput.get()
    if url != '':
        sshUrl = url.replace("https://", "").replace("http://", "").replace('/','')
        str = sshUrl.replace('sis-', '').replace('siap-', '').replace('.salud.gob.sv','').replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('/','')

        try:
            with open(keys_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
        except FileNotFoundError:
            with open(keys_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['url', 'clave'])  # Default headers
                writer.writeheader()
        registroGuardado = buscarClaveGuardada('siap@' + sshUrl)
        if registroGuardado:
            keySaveText.config(text = 'Clave guardada disponible *****')
            hiddenInputSave.delete(0, tk.END) 
            hiddenInputSave.insert(0,registroGuardado['clave'])
            btnCopiarSave.config(state=tk.NORMAL)
            btnOtraClave.config(text='Actualizar clave guardada')
        else:
            keySaveText.config(text = 'Clave guardada no disponible')
            btnOtraClave.config(text='Agregar clave guardada')
            btnCopiarSave.config(state=tk.DISABLED)

        keyText1.config(text = 's1s'+ "*" * (len(str)+4))
        keyText2.config(text = 's14p'+ "*" * (len(str)+4))
        hiddenInput1.delete(0, tk.END) 
        hiddenInput1.insert(0,'s1s'+str+'-s14p')
        hiddenInput2.delete(0, tk.END) 
        hiddenInput2.insert(0,'s14p'+str+'-s14p')
        sshText.config(text = 'ssh siap@' + sshUrl)
        btnCopiar1.config(state=tk.NORMAL)
        btnCopiar2.config(state=tk.NORMAL)
        btnOtraClave.config(state=tk.NORMAL)
        btnSSH.config(state=tk.NORMAL)
        btnOtraClave.config(state=tk.NORMAL)
    else:
        btnCopiar1.config(state=tk.DISABLED)
        btnCopiar2.config(state=tk.DISABLED)
        btnOtraClave.config(state=tk.DISABLED)
        btnSSH.config(state=tk.DISABLED)
        btnOtraClave.config(state=tk.DISABLED)


# Función para copiar el texto al portapapeles
def copiarClave(valor):
    if valor == 1:
        clave = hiddenInput1.get()
        btnCopiar1.config(state=tk.DISABLED)
    elif valor == 2:
        clave = hiddenInput2.get()
        btnCopiar2.config(state=tk.DISABLED)
    elif valor == 3:
        clave = sshText.cget('text')
        btnSSH.config(state=tk.DISABLED)
    elif valor == 4:
        clave = hiddenInputSave.get()
        btnCopiarSave.config(state=tk.DISABLED)
    else:
        clave = None  # Definir un valor por defecto si valor no coincide con 1, 2 o 3

    if clave:
        pyperclip.copy(clave)
        pass

# Función para cerrar la aplicación
def cerrar():
    root.destroy()

def agregarClave():
    urlActual = urlInput.get()
    sshUrl = 'siap@' + urlActual.replace("https://", "").replace("http://", "").replace('/','')

    ventanaClave = tk.Tk()
    ventanaClave.title("Agregar Clave para: " + urlActual)
    ventanaClave.configure(bg=bgApp)
    ventanaClave.resizable(width=False, height=False)
    ventanaClave.geometry("500x200")

    nuevaClaveText = tk.Label(ventanaClave, text="Clave", bg=bgApp, fg=fgText,font=("Arial", 12, "bold"))
    nuevaClaveText.grid(row=0, column=0, padx=5, pady=5)
    nuevaClaveInput = tk.Entry(ventanaClave, width = 45)
    nuevaClaveInput.grid(row=0, column=1, padx=5, pady=5)

    btnGuardar = tk.Button(ventanaClave, text="Guardar", command=lambda:guardarClave(sshUrl, nuevaClaveInput.get(), ventanaClave), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold"))
    btnGuardar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)    

    ventanaClave.mainloop()

def buscar_clave(registros, campo_buscar, valor_buscado):
    for registro in registros:
        if registro[campo_buscar] == valor_buscado:
            return registro
    return None

def actualizar_clave(registro, campo_acualizar, valor_actualizado):
    registro[campo_acualizar] = valor_actualizado

def generar_nueva_clave(url, clave):
     with open(keys_file, 'a', newline='') as csvfile:
        fieldnames = ['url', 'clave']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'url': url, 'clave': clave})

def mostrar_mensaje(msg):
    popup = tk.Toplevel(root)
    popup.title("Atención")
    popup.geometry("300x50")
    label = tk.Label(popup, text=msg)
    label.pack()

    button = tk.Button(popup, text="Aceptar", command=popup.destroy)
    button.pack()
    popup.grab_set()
    popup.wait_window()  # This waits for the popup to be destroyed
    popup.grab_release()

def generar_archivo(url, clave, ventana):
    msg = ''
    with open(keys_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        registros = list(reader) 
        registro_buscado = buscar_clave(registros, 'url', url)
        if registro_buscado:
            actualizar_clave(registro_buscado, 'clave', clave)
            with open(keys_file, 'w', newline='') as csvfile:
                fieldnames = registros[0].keys()  # Get field names from the first row
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()  # Write the header row
                for registro in registros:
                    writer.writerow(registro)
                    
            msg = 'El registro ha sido actualizado de forma exitosa'
        else:
            generar_nueva_clave(url, clave)
            msg = 'El registro ha sido creado de forma exitosa'
        
        mostrar_mensaje(msg)
        generar_keys()
        ventana.destroy()

def guardarClave(url, clave, ventana):
    min = 5
    if len(clave) < min:
        msg = "La clave debe tener al menos "+ str(min)+ ' caracteres'
        mostrar_mensaje(msg)
        return
    #print(url, clave)
    try:
        generar_archivo(url, clave, ventana)
        pass
    except Exception as e:
        print(e)
        mostrar_mensaje('Hubo un error al intenar guardar la clave')

def buscarClaveGuardada(url):
    with open(keys_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        registros = list(reader) 
        registro_buscado = buscar_clave(registros, 'url', url)
        if registro_buscado:
            return registro_buscado
        else:
            return None

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
root.resizable(width=False, height=False)

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
hiddenInput1 = tk.Entry(root)
hiddenInput2 = tk.Entry(root)

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

#Boton clave guardada
keySaveText = tk.Label(root, text="clave guardada", font=("Arial", 9), width = anchokey, anchor="sw", bg=bgApp, fg=fgText)
keySaveText.grid(row=5, column=0, padx=0, pady=5)
btnCopiarSave = tk.Button(root, text="Copiar", command=lambda:copiarClave(4), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold"))
btnCopiarSave.grid(row=5, column=1, padx=5, pady=5)
btnCopiarSave.config(state=tk.DISABLED)
hiddenInputSave = tk.Entry(root)

#Agregar clave
btnOtraClave = tk.Button(root, text="Agregar Clave", command=lambda:agregarClave(), bg=bgBoton, fg=fgBoton, font=("Arial", 9, "bold"))
btnOtraClave.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
btnOtraClave.config(state=tk.DISABLED)

# Botón para cerrar la aplicación
btnCerrar = tk.Button(root, text="Cerrar", command=cerrar)
btnCerrar.grid(row=7, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal
root.mainloop()
