# tipos basicos

# ~ int
# ~ str
# ~ float
# ~ bool

# colecciones

# ~ lista -> matriz
# ~ tupla       --> tuple
# ~ diccionario


mi_tupla = (1, True, "hola", 3.23)
print(mi_tupla[2])
print(type(mi_tupla))

# ~ mi_tupla[2] = 10
# ~ print(mi_tupla[2])

conexion_bd = "127.0.0.1", "root", "qwerty", "clientes"
print(conexion_bd)
print(type(conexion_bd))

conexion_completa =  conexion_bd, "3306", "10"
print(conexion_completa)
print(type(conexion_completa))

print("usuario:", conexion_completa[0][1])
