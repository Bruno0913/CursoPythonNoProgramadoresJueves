import tkinter as tk

alumnos = {}

def ver_lista():
    print("Lista de alumnos:")
    for nombre in alumnos:        
        print(nombre + " - " + str(alumnos[nombre]) + " cursos" )
        

def agregar_alumno():
    nombre = caja_nombre.get()
    cursos = int(caja_curso.get())
    if nombre == "":
        print("Error: no ingreso un nombre valida")
    else:
        alumnos[nombre] = cursos
        print("¡El alumno fue añadido a la lista!")
        
def ver_cursos():
    nombre = caja_nombre.get()
    if nombre in alumnos:
        print("El alumno", nombre, "tiene", alumnos[nombre], "cursos")
    else:
        print("No existe el alumno")

ventana = tk.Tk()
ventana.title("Proyecto Integrador")
ventana.config(width=500, height=280)

boton_lista = tk.Button(text = "Ver lista de alumnos", command=ver_lista)
boton_lista.place(x=10, y=10)

etiqueta_nombre = tk.Label(text="Nombre alumno:")
etiqueta_nombre.place(x=10, y=60)

caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=60, width=150, height=20)

etiqueta_curso = tk.Label(text="Cursos:")
etiqueta_curso.place(x=10, y=100)

caja_curso = tk.Entry()
caja_curso.place(x=110, y=100, width=50, height=20)

boton_agregar = tk.Button(text = "Agregar a la lista", command=agregar_alumno)
boton_agregar.place(x=10, y=150)

boton_curso = tk.Button(text = "Ver cantidad de cursos", command=ver_cursos)
boton_curso.place(x=120, y=150)


ventana.mainloop() 
