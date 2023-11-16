'''
Mediante el uso de ciclos realice los siguientes ejercicios:

Recibir un número positivo N, comenzando desde 10 hasta N obtenga la suma de los números pares y el promedio de los impares.

'''
#Ejercicio c

def calcular(arrCalculo):
    suma = 0
    for num in arrCalculo:
        print(f"El cuadrado es: {num**2}")
        suma += num**2
    print(f"La suma de los cuadrados es: {suma}")
        
    
userInput = -1
print(f"Vamos a calcular la suma de los pares y el promedio de los impares\n"  +
      "desde el número que ingreses hasta el 10")
while userInput < 10:
    userInput = int(input("Ingresa el Número TOPE: "))
arrPar = []
arrImpar = []

for i in range(10, ( userInput + 1 )):    
    if i % 2 == 0:        
        arrPar.append(i)
    else:
        arrImpar.append(i)
sumPar = sum(arrPar)
sumImpar = sum(arrImpar)
promImpar = sumImpar / len(arrImpar)

print(f"Suma Pares: {sumImpar}")
print(f"Promedio Impares: {promImpar}")


            




    
            
    
        


    
        

    
