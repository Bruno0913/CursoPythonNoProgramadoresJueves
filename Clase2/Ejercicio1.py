# ~ Escribir un programa que dado el precio de un producto (a definir x el alumno)
# ~ calcule el precio del producto mas IVA
# ~ El programa debe informar el precio del producto con y sin iva.
# ~ El IVA es el 21%

precio = 100
iva = 21

totiva = precio * iva / (100)
precioproducto = precio + totiva

print ("El precio del producto sin iva es",precio)
print ("El precio del producto con iva es",precioproducto)
print ("El precio del producto con iva es",precio + precio * 0.21)
