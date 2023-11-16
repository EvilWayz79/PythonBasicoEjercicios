'''
Mediante el uso de ciclos realice los siguientes ejercicios:
a.  Al recibir como datos un grupo de números enteros positivos, para terminar el ciclo el usuario deberá ingresar el número cero (0), calcule el cuadrado de estos números.
        Imprima el cuadrado de los números recibidos y al final la suma de los cuadrados.
b.  Ingrese a una serie de números por teclado e indique cuál es el mayor. Para terminar el programa el usuario debe ingresar el valor 0 (cero).
c.  Recibir un número positivo N, comenzando desde 10 hasta N obtenga la suma de los números pares y el promedio de los impares.
d.  Escriba las tablas de multiplicar de un número ingresado por el usuario la tabla debe multiplicar hasta el 15
e.  Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo como el de más abajo.
        triangulo numeros.JPG
f.  Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''
#Ejercicio a

def calcular(arrCalculo):
    suma = 0
    for num in arrCalculo:
        print(f"El cuadrado es: {num**2}")
        suma += num**2
    print(f"La suma de los cuadrados es: {suma}")
        
    
arrNum = []
print(f"Calcula el cuadrado de Números enteros positivos, ingresa 0 para calcular resultados")
userNum = -1

while userNum != 0:
    userInput = 0
    try:      
        userInput = int(input("Ingresa el número: "))  
        while userInput < 0:
            userInput = int(input("Ingresa el número: "))  
    except ValueError:
        print("Solo valores numéricos enteros")
        tamArr = len(arrNum)
        if tamArr > 0:
            print(f"ERROR! existen {tamArr} datos validos Calculando resultados...")
            calcular(arrNum)
            break #Sale calculando los datos validos ingresados
    userNum = userInput
    if userNum != 0:
        arrNum.append(userNum)
    else:
        calcular(arrNum)



    
            
    
        


    
        

    
