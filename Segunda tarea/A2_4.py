#Act.4 Numer Fibonacci.


n = int(input("Ingrese la cantidad de n numeros que desees ver en la lista de fibonacci:"))

if (n > 50):
      print("Errororrrr, debe ser menor a 50")
     

def fibo(n):
    a = 0
    b = 1
    fibo =[a,b]
    for i in range (2, n):
        c = a + b
        fibo.append(c)
        a = b
        b = c
    return fibo

print (fibo(20))
    
   
