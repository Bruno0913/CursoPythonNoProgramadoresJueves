# ~ 1. Elevar b al cuadrado.
# ~ 2. Multiplicar 4 por a y por c.
# ~ 3. Restar el resultado de (2) al resultado de (1).
# ~ 4. Calcular la raíz cuadrada del resultado de (3).
# ~ 5. Sumar el resultado de (4) a -b.
# ~ 6. Dividir el resultado de (5) por 2a.
# ~ 7. Restar el resultado de (4) a -b.
# ~ 8. Dividir el resultado de (7) por 2a.

# concatenacion de cadenas = print(cadena1 + cadena2)
# concatenacion de cadenas = print(cadena1, cadena2, cadena3)

a = 1
b = 1
c = -6

paso1 = b ** 2
#print(paso1)
paso2 = 4 * a * c
#print(paso2)
paso3= paso1 - paso2
#print(paso3)
paso4 = paso3 ** (1/2)
#print(paso4)
paso5 = -b + paso4
#print(paso5)
paso6 = paso5 / (2 * a)
#print("Primer resultado", paso6)
paso7 = -b - paso4
#print(paso7)
paso8 = paso7 / (2 * a)
#print("Segundo resultado",  paso8)
print("Los resultados son", paso6, "y", paso8)
