# diccionarios -> dict

# miDiccionario = {clave1: valor1, clave2:valor2, ....., claven: valorn}

miDiccionario = {'nombre':'carlos', 'edad':22, 'cursos': ['Python', 'Java', 'C#']}

print(miDiccionario)
print(type(miDiccionario))

# ~ print(miDiccionario['nombre'])
# ~ print(miDiccionario['edad'])
# ~ print(miDiccionario['cursos'])

for key in miDiccionario:
    print(key, ":", miDiccionario[key])
    
print("----------------------------")

materias = {}

materias["lunes"] = [6150, 3356]
materias["martes"] = [6150, 3356, 4444]
materias["miercoles"] = [3356]
materias["jueves"] = []
materias["viernes"] = [6150, 2222]

for i in materias:
    print(i, ":", materias[i])
    
materias["lunes"] = [7777, 3356]
print("cambio lunes:", materias["lunes"])

print("----------------------------")

diccionario2 = {0:"cero", 1:"uno", 2:"dos", 3:"tres"}
print(diccionario2)
print(type(diccionario2))
print(diccionario2[1])


