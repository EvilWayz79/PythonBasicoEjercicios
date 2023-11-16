# Tuplas
# Inmutables
tupla = (1, "Hello", 3.4)
print(tupla)
j=0
for i in tupla:
    print(f"posicion {j}", i)
    j+=1

# Listas
# Mutables
lista = [1, 2, 3.45, 9, 8, 6]
print(lista)
print(lista[0])
lista.append(6)
print(lista)
lista_ = [6,7,8]
lista.extend(lista_)
print(lista)
lista.remove(2)
print(lista)
lista.pop(2)
print(lista)
print("Index de 3.45: ", lista.index(3.45))
print("Numero de veces 6: ", lista.count(6))
lista.sort() #OJO!!! NO FUNCIONA CUANDO ES LISTA MIXTA CON CADENAS
print(lista)
lista.sort(reverse=True)
print(lista)

# Diccionarios
dcn = {"nombre":"carla", "apellido":"Corrales", "edad":25}
print(dcn)
print(dcn.keys())
print(dcn.values())



