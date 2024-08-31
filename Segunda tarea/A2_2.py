#Act 2. Factorial de un num.
f = int(input("Ingrese un numero:"))
if f>20:
    print("El número tiene que ser menor a 20. Errrorerro.")

fact=1
for i in range(1, f+1):
    fact*=i
print ("El factorial de", f, "es:", fact)
    
