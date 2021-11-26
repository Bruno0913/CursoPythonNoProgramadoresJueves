# ~ Escribir un programa que use una funcion que compare dos cadenas de texto. 
# ~ Si las cadenas son iguales o no devolver un valor booleano que lo indique

# ~ Las cadenas de texto deben solicitarse desde el programa principal.
# ~ y dependiendo si son iguales o diferentes, devolver un mensaje
# ~ que lo indique.
# ~ Ej, las cadenas son iguales o las cadenas son diferentes

def iguales(texto1, texto2):
    return texto1 == texto2
    

print("-----inicio programa-----")

t1 = input("Ingrese palabra 1: ")
t2 = input("Ingrese palabra 2: ")

comparar = iguales(t1, t2)

if comparar:
    print("Los valores son iguales")
else:
    print("Los valores son distintos")


print("-----fin programa-----")
