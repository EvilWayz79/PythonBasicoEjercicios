# practica funciones

""" 
def imprimir_mensaje():
    print("Mensaje: ")
    print("Hola Mundo!! Esta es mi primera función en Python 😎")
    
if __name__ == '__main__':
    imprimir_mensaje()
    imprimir_mensaje()
    imprimir_mensaje()
 """
# Funcion para detectar si un numero es par o impar
""" 
def detectNum(num):
    if num%2 == 0:
        return "par"
    else :
        return "impar"


if __name__ == '__main__':
    print(f"El número es: ", detectNum(int(input("Ingresa el número: "))) ) 
"""
    
#Realizar una función que me permita realizar el factorial de un número 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == '__main__':
    while True:
        try:
            num = int(input("Ingresa un número mayor a 0: "))
            if num < 0:
                print("No existe factorial para menores a 0.")
            else:
                print("El factorial de", num, "es: ", factorial(num))
                break
        except ValueError:
            print("Ingresa Números Positivos!.")