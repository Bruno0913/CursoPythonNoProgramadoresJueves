# ~ Escribir un programa que pida al usuario una cantidad de alumnos a cargar.
# ~ Luego pedir los nombres de los alumnos segun la cantidad ingresada
# ~ en el paso anterior.
# ~ Por ultimo el programa debe imprimir el nombre de cada alumno con el
# ~ siguiente formato:
# ~ nombre alumno: {nombre}


alumnos = []

# Paso 1: pedir cantidad de alumnos a cargar
numero_alumnos = int(input("Ingresa numero de alumnos: "))

# Paso 2: cargar la lista

# ~ i = 0
# ~ while i < numero_alumnos:
    # ~ alumnos.append(input("Ingresa nombre alumno" + str(i) + ": "))
    # ~ i = i +1
    
for i in range(numero_alumnos):
	alumnos.append(input("Ingresa nombre alumno" + str(i) + ": "))

# Paso 3: mostrar los valores de la lista

# ~ for alumno in alumnos:
    # ~ print("Nombre de alumno: ", alumno)

j = 0
while j < numero_alumnos:
    print("Nombre de alumno: ", alumnos[j])
    j = j + 1
    

