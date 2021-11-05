
# Conjuncion (and)

a = 1 + 8

if a >= 1 and a <= 10:
    print("a esta entre 1 y 10")
else:
    print("a no esta entre 1 y 10")
    

edad = 10

if edad >= 16 and edad < 70:
    print("Votacion obligatoria")
elif edad >= 70:
    print("Votacion opcional")
else:
    print("No puede votar")
    
# Disyuncion (OR)

if a > 7 or a < 0:
    print("a es mayor a siete o negativo")
else:
    print("a esta entre 1 y 9")
    
# OPERADOR NOT
nota = 3
aprobado = nota >= 4

# not True == False
# not False == True
if not aprobado:
    print("Esta desaprobado")

if aprobado == False:
    print("Esta desaprobado")
    





