'''
Mediante el uso de ciclos realice los siguientes ejercicios:

Ingrese a una serie de números por teclado e indique cuál es el mayor. Para terminar el programa el usuario debe ingresar el valor 0 (cero).

'''
#Ejercicio b

def calcular(arrCalculo):
    print(f"El número mayor es: {max(arrCalculo)}")
        
    
arrNum = []
print(f"Ingresa una serie de números y te indicaré cual es el mayor, ingresa 0 para terminar")
userNum = -1

while userNum != 0:
    userInput = 0
    try:      
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



    
            
    
        


    
        

    
