# ~ Escribir un programa que almacene en una lista los siguientes precios
# ~ de productos: 50, 75, 46, 22, 80, 65, 8.
# ~ Se debe mostrar por pantalla el menor y mayor de los precios.
# el precio menor es: {menor} y el precio mayor es: {mayor}

#precios = [50, 75, 46, 100, 80, 65, 8, 2]

precios = [0, -75, -46, -100, -80, -65, -8, 2]

menor = precios[0]
mayor = 0

for precio in precios:
    if precio < menor:
        menor = precio
    elif precio > mayor:
        mayor = precio
        
print("el precio menor es: ",menor, "y el precio mayor es:",mayor)
 
    
    
    
# ~ lista_precios = [50,75,46,22,80,65,8]

# ~ for precio in lista_precios:
    # ~ if precio > 75:
        # ~ print( "y el precio mayor es: ", precio)
    # ~ elif precio < 22:
        # ~ print("el precio menor es: ", precio)
