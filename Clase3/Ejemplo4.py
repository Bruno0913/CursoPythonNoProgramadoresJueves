# ~ Escribir un programa que pida 3 notas (de 1 al 10) de un alumno por consola.
# ~ El programa debe calcular el promedio y devolver si aprobo sabiendo
# ~ que se aprueba con una nota mayor a 4.

NotaA = int(input("Ingrese primer nota: "))
NotaB = int(input("Ingrese primer nota: "))
NotaC = int(input("Ingrese primer nota: "))

Promedio = (NotaA + NotaB + NotaC) / 3

if Promedio > 4:
	print("Usted esta aprobado")
else:
	print("Usted esta desaprobado")
