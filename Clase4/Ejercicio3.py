
#  Bucles

# while: importante tener una sentencia de corte de bucle.

# for

if 1 < 5:
    print("hola mundo - IF")
    
########-------WHILE------------############

"""
while condicion:
    bloque de codigo
"""
    
i = 0
while i < 5:
    print("hola mundo - WHILE")
    i = i + 1
    
    
print("Fin del program")
print("------------------------------")

########-------FOR------------############

"""
1-
for variable_iteracion in variable_lista:
    bloque de codigo

2-
for variable_iteracion in range():
    bloque de codigo
"""

alumnos = ["Juan", "Sofia", "Leandro", "Sol", "Ana"]
print("Antes del for")
for alumno in alumnos:
    print("Hola", alumno)
    
print("Fin del for")
