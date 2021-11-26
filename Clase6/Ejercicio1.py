
# ~ def nombre_funcion:
    # ~ bloque_codigo
    

def sumar(a, b):
    resultado = a + b
    # ~ resultado2 = resultado
    # ~ print("la variable numero1 es", numero1)
    return resultado
    
    
print("-----inicio programa-----")

numero1 = 50
numero2 = 75

suma = sumar(numero1, numero2)
print("la suma es", suma)

if suma > 100:
    suma = suma +100
else:
    suma = suma - 100
    
print("la suma es", suma)

#print("resultado en funcion", resultado)


print("-----fin programa-----")
