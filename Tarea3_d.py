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
#Ejercicio d

numeroMultiplica = int(input("Ingresa el numero a multiplicar: "))
print(f"Tabla de multiplicar del {numeroMultiplica}")
for i in range(0, (15 + 1)):
    print(f"{numeroMultiplica} * {i} = {numeroMultiplica * i}")

    
        

    
