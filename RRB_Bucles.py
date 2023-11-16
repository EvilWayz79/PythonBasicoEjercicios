import math


numero = int(input("Digite un numero: "))
while  numero < 0 :
    print("Error -> No existen raices de negativos")
    numero = int(input("Digite un numero: "))
print(f"\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}")

for i in range(8):
    print("Hola Mundo", (i+1) )
    
for i in [2,10,3,4,"Texto 1", 6, "texto 2", "😎😎"]: #ja!
    print(i)
coleccion = {"Alejandro":22, "Maria":23, "Jose":45, "Luis":12}

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")
