# ~ Escribir un programa que evalue los rangos de una variable "a"
# ~ Si la variable esta entre 1 y 10 escribir un mensaje que indique que dicha variable
# ~ esta en ese rango.
# ~ Lo mismo si la variable esta entre 11 y 20 y si esta entre 21 y 30.
# ~ En el caso que no este en ningun rango, indicar un mensaje
# ~ que describa esa situacion.
# ~ Nota: incluir los valores extremos de los rangos en la comparacion.

a = 12

if a >= 1 and a <= 10:
    print("Esta en el rango de 1 a 10")
elif a >= 11 and a <= 20:
    print("esta entre 11 y 20")
elif a >= 21 and a <= 30:
    print("esta entre 21 y 30")
else:
    print("no esta en ningun rango")
