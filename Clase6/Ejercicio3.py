# ~ Realizar un programa que use una funcion que imprima los numeros segun 
# ~ un rango dado por parametro.
# ~ ejemplo: imprimirNumeros(1,10) -> 1....10 (en cada linea)
         # ~ imprimirNumeros(25,35) -> 25....35 (en cada linea)
         
# Se puede pedir al usuario los valores de los rangos, limite inferior
# y limite superior, desde el programa principal

# ~ se podria usar -> range()

def imprimir_numeros(inicio,final):
    for numero in range(inicio,final + 1):
        print(numero)

inicio = input("Ingrese valor de inicio: ")
inicio = int(inicio)

final = input("ingrese valor final: ")
final = int(final)

imprimir_numeros(inicio,final)
