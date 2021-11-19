
alumnos = []

# alumnos = [["Ana", 4], ["Juan", 3], ["Sofia2, 5], ["Luis", 4]]

while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")
    
    opcion = int(input("Ingrese un numero de opcion: "))
    
    if opcion == 1:
        if len(alumnos) > 0:
            print("Lista de alumnos:")
            for alumno in alumnos:
                nombre = alumno[0]
                cursos = alumno[1]
                print(nombre + " - " + str(cursos) + " cursos" )
                #print(alumno[0] + " - " + str(alumno[1]) + " cursos" )
        else:
            print("No hay alumnos en la lista")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos: "))
        if nombre == "":
            print("Error: no ingreso un nombre valida")
        else:
            alumnos.append([nombre, cursos])
            print("¡El alumno fue añadido a la lista!")
    elif opcion == 3:        
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")


print("¡Gracias por utilizar el programa!")
    
    





