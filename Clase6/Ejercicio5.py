import tkinter as tk

def saludar():
    nombre = caja1.get()
    print("Hola mundo para", nombre)
    
def imprimir_numeros():
    for i in range(1,11):
        print(i)

#crear ventana
ventana = tk.Tk()

#configurar titulo
ventana.title("Mi primer aplicacion")

#configurar tamaño
ventana.config(width=500, height=400)

#Crear un boton
boton1 = tk.Button(text = "Saludar", command=saludar)

#darle un tamaño y una ubicacion
boton1.place(x=30, y=50, width=100, height=40)

boton2 = tk.Button(text = "Imprimir Nros", command=imprimir_numeros)
boton2.place(x=30, y=100, width=200, height=40)

# crear caja de texto
caja1 = tk.Entry()
caja1.place(x=30, y=220, width=200, height=25)

# crear una etiqueta
etiqueta_nombre = tk.Label(text = "Ingrese su nombre")
etiqueta_nombre.place(x=30, y=195, width=200, height=25)


# mostrar ventana
ventana.mainloop() 

#print("hola mudo")
