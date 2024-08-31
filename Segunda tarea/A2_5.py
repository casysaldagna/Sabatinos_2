#Act. 5 Contar vocales.

texto = input("Ingresa un texto:")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É','Í', 'Ó', 'Ú']
conta = 0
vocal = []

for letra in texto:
   if letra in vocales:
       conta += 1
       vocal.append (letra)
        
print ("El texto:", texto,  "tiene", conta, "número de vocales.")
