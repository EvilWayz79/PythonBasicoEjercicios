# obtener el mayor de 3 números

numero1 = int(input("Ingresa numero 1:" ))
numero2 = int(input("Ingresa numero 2:" ))
numero3 = int(input("Ingresa numero 3:" ))
resultado = 0

if(numero1 > numero2):
    resultado = numero1
else: resultado = numero2
if(resultado < numero3):
    resultado = numero3

print(f"El número mayor es: {resultado}")

