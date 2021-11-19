# ~ Crear un programa que genere una tupla ya predefinida del 1 al 10.
# ~ El programa debe pedir al usuario un indice por teclado y se debe mostrar
# ~ el valor del elemento de la tupla en ese indice.
# ~ Verificar que sea un indice valido
# ~ en el caso de que sea un indice no valido mostrar un mensaje de error


tupla = 1,2,3,4,5,6,7,8,9,10

indica_valor = int(input("Que fila busca: "))

while indica_valor < 0 or indica_valor >= len(tupla):
    print("Valor invalido")
    indica_valor = int(input("Que fila busca: "))
    

print(tupla[indica_valor])

# ~ tupla = 1,2,3,4,5,6,7,8,9,10

# ~ indice = int(input("Que indice busca: "))

# ~ if indice >= 0 and indice < len(tupla):
    # ~ print(tupla[indice])
# ~ else:
    # ~ print("Indice no valido")
