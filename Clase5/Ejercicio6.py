alumnos = {}

# alumnos = [["Ana", 4], ["Juan", 3], ["Sofia2, 5], ["Luis", 4]]
# alumnos = {"Ana": 4, "Juan": 3, "Sofia": 5, "Luis": 4}

while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Ver la cantidad de cursos de un alumno")
    print("4 - Salir.")
    
    opcion = int(input("Ingrese un numero de opcion: "))
    
    if opcion == 1:
        print("Lista de alumnos:")
        for nombre in alumnos:            
            cursos = alumnos[nombre]
            print(nombre + " - " + str(cursos) + " cursos" )
    elif opcion == 2:
        nombre = input("Ingrese el nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos: "))
        if nombre == "":
            print("Error: no ingreso un nombre valida")
        else:
            alumnos[nombre] = cursos
            print("¡El alumno fue añadido a la lista!")
    elif opcion == 3:        
        nombre = input("Ingrese el nombre del alumno a consultar: ")
        if nombre in alumnos:
            print("El alumno", nombre, "tiene", alumnos[nombre], "cursos")
        else:
            print("No existe el alumno")
    elif opcion == 4:        
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")


print("¡Gracias por utilizar el programa!")
