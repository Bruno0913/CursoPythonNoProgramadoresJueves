# Tipos basicos

a = 5 # Entero (int)
pi = 3.14 # Numero de coma flotante (float)
saludo = "Hola" # cadenas de texto (str)
encendido = True # Booleanos (bool)


# Tipos estructurados

# ~ Listas
# ~ Tuplas
# ~ Diccionarios

# -------Listas-------------

alumno1 = "Matias"
alumno2 = "Sofia"
alumno3 = "Juan"

# ~ print(alumno1)
# ~ print(alumno2)
# ~ print(alumno3)


#crear lista
# lista -> list
alumnos = ["Matias", "Sofia", "Juan"]
print(alumnos)
print(type(alumnos))

#Indice = posicion
x=2
print(alumnos[x])
print("Hola", alumnos[3-x])

# -------Ejemplo programa con y sin lista-------------

# programa sin lista

alumno1 = "Matias"
alumno2 = "Sofia"
alumno3 = "Juan"
alumno4 = "Martina"

indice = int(input("Ingrese un indice (1-4): "))

if indice == 1:
    print("Hola", alumno1)
elif indice == 2:
    print("Hola", alumno2)
elif indice == 3:
    print("Hola", alumno3)
elif indice == 4:
    print("Hola", alumno4)


# programa con lista


alumnos = ["Matias", "Sofia", "Juan", "Martina" ]
indice = int(input("Ingrese un indice: "))
print("Hola", alumnos[indice])


# ---------RESUMEN LISTA------------

# Agregar un elemento al final
lista.append(elemento)

# Agregar un elemento en un indice particular
lista.insert(indice, elemento)

# Borra un elemento
del lista[indice]

# Reemplazar un elemento por otro
lista[indice] = elemento

# Ver cantidad de elementos de una lista
len(lista)


















