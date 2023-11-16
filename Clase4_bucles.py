# En python solo existen while y for, ningun otro
# 
'''
Mediante el uso de ciclos realice los siguientes ejercicios:
Ejercicio 1 : Muestre la siguiente secuencia de números : 10,9,7,5,4,3,1

Ejercicio 2: Muestre los 10 primeros múltiplos de 3

Ejercicio 3: Obtener el factorial de un numero ingresado por el usuario 
'''
# Ejercicio 1

a = 10
b = 1
c = 2

while a > 0:
    print("Res: ", a)
    if a%5 == 0:
        a -= 1        
    else:
        a -= 2

count = 1
for i in range(1, 33):    
    if i%3 == 0:
        print(f"pos {count}: ", i)
        count += 1

nFactorial = int(input("NumeroFactorial: "))
while nFactorial < 0:
    nFactorial = int(input("NumeroFactorial: "))
res = 1
for i in range(1, (nFactorial + 1) ):    
    res *= i
print(f"ResFactorial: ", res)


