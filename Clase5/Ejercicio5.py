# ~ Escribir un programa que pregunte al usuario su nombre, edad, direccion y telefono.
# ~ La informacion debe guardarse en un diccionario.
# ~ y el programa debe mostrar por pantalle el siguiente mensaje:
    
# ~ <nombre> tiene <edad> años, vive <direccion> y su numero de telefono es <telefono>

# ~ nombre= input("Ingrese su nombre:")
# ~ edad = input("Ingrese su edad: ")
# ~ direccion = input("Ingrese su direccion: ")
# ~ telefono = input("Ingrese su telefono: ")

# ~ persona = {"nombre": nombre, "edad": edad, "domicilio": direccion, "telefono": telefono}

persona = {"nombre": input("Ingrese su nombre:"), "edad": input("Ingrese su edad: "), "domicilio": input("Ingrese su direccion: "), "telefono": input("Ingrese su telefono: ")}

print(persona["nombre"],"tiene", persona["edad"], "años, vive", persona["domicilio"],"y su numero de telefono es", persona["telefono"])
