# ~ Escribir un programa que pregunte al usuario 5 edades.
# ~ Se debe mostrar como resultado, las edades en una lista
# ~ ordenada de manera inversa 

# ordernar elementos de una lista
# - lista.sort()
# - lista.sort(reverse=True)


lista_edades = []

lista_edades.append(int(input("Ingresa primer edad: ")))
lista_edades.append(int(input("Ingresa segunda edad: ")))
lista_edades.append(int(input("Ingresa tercera edad: ")))
lista_edades.append(int(input("Ingresa cuarta edad: ")))
lista_edades.append(int(input("Ingresa quinta edad: ")))

lista_edades.sort(reverse=True)

print(lista_edades)
