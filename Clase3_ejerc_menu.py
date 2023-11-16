autor = "RRB"

print(f""" Progama demo de menu en python
      Autor: {autor}
      -👌👌👌🤦‍♂️👌👌👌-
      Menu que gestiona opciones
      Las opciones posibles son:
      1. Sueldo
      2. Par o impar
      3. Multiplo de 5
      4. Division si el numerador es mayor que el denominador
      """)
print("Hola, dame tu nombre: ")
usr = input()
opt = input(f"Bienvenido, {usr} Ingresa la opcion que vas a seleccionar: ")
if opt == "1":
    edad = int(input("Ingrese edad😎: "))
    prof = input("Ingrese Profesion🎶: ")
    sueldo = 0

    if(edad > 18 and prof == "abogado") :
        sueldo = 3000
        print(f"Su sueldo al año es de {sueldo}")
        
    elif 30<edad<60 and prof == "ingeniero":
        sueldo = 3500
        print(f"Su sueldo al año es de {sueldo}")
    
elif opt == "2":
    numero_par = int(input("Es par o impar?😁: "))
    test_par = "Es par"
    if(numero_par % 2 != 0):
        test_par = "No es par"
    print(f"{test_par}")
elif opt == "3":
    mult_cinco = int(input("Es Multiplo de 5?👌: "))
    test_cinco = "Es multiplo de 5"
    if(mult_cinco % 5 != 0):
        test_cinco = "No es multiplo de 5"
    print(f"{test_cinco}")
elif opt == "4":
    numerador = int(input("Ingresa Numerador✌️: "))
    denominador = int(input("Ingresa Denominador🤞: "))
    resultado = "No se divide"
    if(numerador > denominador):
        resultado = numerador / denominador
    print(f"{resultado}")
else:
    print("La opcion no es valida")
    