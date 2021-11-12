# ~ Escribir un programa que almacene una cadena de texto: "contraseña"
    # ~ en una variable. Buscar un mecanismo que pregunte al usuario
    # ~ por la contraseña hasta que introduzca la contraseña correcta.
# ~ en el caso de que coincidan los valores, devolver el 
# ~ mensaje: contraseña correcta.

contrasenia = "contrasenia"

ingresa_contrasenia = input("Ingresa contrasenia: ")

while ingresa_contrasenia != contrasenia:
    print("Contrasena incorrecta")
    ingresa_contrasenia = input("Ingresala de vuelta: ")

print("contrasenia correcta")
