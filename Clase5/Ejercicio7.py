# Funciones

# ~ input()
# ~ print()
# ~ lista.append()
# ~ int()
# ~ str()

# ~ def nombre_funcion:
    # ~ bloque_codigo
    

def imprimir_mensajes(nombre_editor, lenguaje, año=2000):
    print("Hola mundo")
    print("desde " + lenguaje)
    print("y desde " + nombre_editor + ".")
    print("En el año", año)

print("-----inicio programa-----")

imprimir_mensajes("Geany", "Python")

a = 5
b = 7
c = a + b
print(c)

imprimir_mensajes("Visual Studio Code", "Java", 2021)

print("-----fin programa-----")
