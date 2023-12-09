'''
Proyecto final que haga uso de todas las habilidades adquiridas en el curso de python básico dictado
durante la maestría de BIG Data
                                                                                        Rubén Recalde
Vamos a realizar el concepto de un album de cromos coleccionables, donde el usuario adquiera paquetes
de 3 cromos cada uno
El total de cromos es 24, los generaremos al inicio del programa ya que dentro de la introducción no
    existe conexíón a base de datos
Cada sobre tiene 3 cromos que son seleccionados randomicamente
Existen 4 tipos de cromos: Fuego, Agua y Tierra, Aire cada uno con 6 instancias de cromos
Cada cromo consta de código identificador (entero numerico del 1 al 24), nombre del cromo (texto), tipo de cromo (F, Agua, T, Aire)
Pueden salir cromos repetidos, los cromos repetidos serán desechados
los cromos nuevos se añadiran automáticamente al album
luego de abrir un paquete de cromos, se mostrará el album del usuario
No existe memoria permanente, los datos se borrarán al salir de la aplicación                                                                                        
Existe un menú en el cual el usuario puede:
    1. Visualizar su album
    2. Comprar Cromos
    3. Ver porcentaje de cromos de cada elemento
    0. Salir
'''
class cromo:
    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.Nombre_cromo = nombre
        self.Tipo_de_cromo = tipo

#item = cromo(1, "TestN", "TestTipo")
#print(f"Codigo: {item.codigo} Nombre: {item.Nombre_cromo} Tipo: {item.Tipo_de_cromo}")

def menu(nombre_usuario):    
    print(f"""Hola {nombre_usuario}! Bienvenido a tu
    Album de los desastres naturales más famosos 
    relacionados con sus elementos naturales     
      -🫗🔥🌬️🌐-
      Menu que gestiona opciones
      Las opciones posibles son:
      1. Visualiza tu album
      2. Compra 1 sobre de cromos
      3. Ver porcentaje de cromos de cada elemento
      0. Salir
      """)
    
def generador_cromos():
    #usamos diccionarios y lista
    agua = {"Jamaica":1, "Portugal":2, "Haiti":3, "Venezuela": 4, "Panama":5, "Japon":6}
    aire = {"Katrina":7, "Harvey":8, "Maria":9, "Sandy": 10, "Irma":11, "Ike":12}
    fuego = {"Boston":13, "Londres":14, "Roma":15, "Chicago": 16, "Halifax":17, "Tokio":18}
    tierra = {"Valdivia":19, "Sumatra":20, "Kamchatka":21, "Ecuador": 22, "Colombia":23, "Sumatra":24}
    album_completo = [agua, aire, fuego, tierra]
    return album_completo

usuario = input("Dime tu nombre: ")
userInput = -1

while userInput != 0:
    menu(usuario)
    userInput = int(input("Ingresa tu opción: "))
    if userInput == 1:
        album_completo = generador_cromos()
        for i in range(len(album_completo)):
            print(f"{i}") 
    
print(f"Gracias {usuario}! ♥️ Vuelve pronto ♥️")    


    
    
    



