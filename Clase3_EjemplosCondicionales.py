# Si la edad es mayor a 18 y la prof es abogado => sueldo de 3000 al año
# Si la edad es mayor a 30 y menor a 60 y la profesion es Ingeniero => 3500 al año

edad = int(input("Ingrese edad: ")) #18
# edad1 = int(input("Ingrese edad1: ")) #20
prof = input("Ingrese Profesion: ")

""" if edad > edad1 :
    print(f"{edad} es mayor")
if edad1 > edad:
    print(f"{edad1} es mayor")
if edad == edad1:
    print(f"{edad} es igual a {edad1}")
 """    
sueldo = 0

if(edad > 18 and prof == "abogado") :
    sueldo = 3000
    print(f"Su sueldo al año es de {sueldo}")
    
elif 30<edad<60 and prof == "ingeniero":
    sueldo = 3500
    print(f"Su sueldo al año es de {sueldo}")
    
    

    

    
    
    

