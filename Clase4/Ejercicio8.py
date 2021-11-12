# break: sale del bucle de manera definitiva

# continue: sale de la iteracion y continua con la siguiente

print("-------break while----------------")
i = 0
while i <= 10:
    print(i)
    i = i + 1
    if i == 5:
        break

print("---------break for--------------")

for i in range(11):
    print(i)
    if i == 5:
        break


print("----------continue while-------------")
i = 0
while i <= 10:
    print(i)
    i = i + 1
    if i == 5:
        continue
    print("hola", i)
        
        
        
        
        
        
        
        
        
