#Ej. 1 Suma de números pares.

suma = 0
for i in range (0, 100):
    if i%2 == 0:
        print("Los num pares del 1 al 100 son:", i)
        suma = suma+i

print("Y la suma de los num pares son:", suma)    
        
