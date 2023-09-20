#Secuencia Collatz 

elementos = []
num_elementos = (10)

for i in range(10):
    elementos.append(int(input("Ingrese un numero natural cualquiera:")))

print(elementos)
suma_elementos = sum(elementos)
prom_elementos = int(suma_elementos / num_elementos)

print("Secuencia Collatz para el numero:",prom_elementos)
print(prom_elementos)
while prom_elementos < 258 and prom_elementos != 1:
    if prom_elementos % 2 == 0:
        prom_elementos = int(prom_elementos / 2)
        print(prom_elementos)
    else:
        prom_elementos = int(prom_elementos*3 + 1)
        print(prom_elementos)
print("Ha salido de la secuencia")   