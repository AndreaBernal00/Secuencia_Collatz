 #Secuencia Collatz 

elementos = []
num_elementos = (10)

for n in range(num_elementos):
    elementos.append(int(input("Ingrese un numero natural cualquiera:")))

suma_elementos = sum(elementos)
prom_elementos = int(suma_elementos / num_elementos)

if 0 < prom_elementos < 258:
    print("\nSecuencia Collatz para el numero:",prom_elementos)
    while prom_elementos != 1:
        if prom_elementos % 2 == 0:
            prom_elementos = int(prom_elementos / 2)
            print(prom_elementos)
        else:
            prom_elementos = int(prom_elementos*3 + 1)
            print(prom_elementos)
    print("\nHa salido de la secuencia") 
else:
   print("\nLa Secuencia Collatz no es valida para el numero",prom_elementos)
