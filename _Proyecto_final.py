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
#imports
import random



#Constantes
_TOTAL_CROMOS = 24
_AGUA = "agua"
_AIRE = "aire"
_FUEGO = "fuego"
_TIERRA = "tierra"

_RED = '\033[31m'
_GREEN = '\033[32m'
_BLUE = '\033[34m'
_YELLOW = '\033[33m'
_RESET = '\033[0m'

colors = [_BLUE, _YELLOW, _RED, _GREEN]

#Globales
classAlbum = [] #global porque es el objetivo del programa
cromos_usuario = [] #lista de codigos de cromos que tiene el usuario


class cromo:
    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.Nombre_cromo = nombre
        self.Tipo_de_cromo = tipo

def menu(nombre_usuario):    
    print(f"""\nHola {nombre_usuario}! Bienvenido a tu Album de los lugares de los
    desastres naturales más famosos relacionados con sus elementos naturales     
      -   🌊   🌀   🔥   🌋   -      
      Aquí tu puedes:
      1. Visualizar el detalle de tus cromos      
      2. Adquirir 1 sobre de cromos
      3. Ver porcentaje de cromos que tienes de cada elemento
      4. Ver tu album lleno (cromos obtenidos se muestran entre - )
      0. Salir
      """)
    
def generador_cromos():
    #usamos diccionarios y lista
    agua =  ({"tipo":"agua", "nombre":"Jamaica", "codigo":1}, 
    {"tipo":"agua", "nombre":"Portugal", "codigo":2}, 
    {"tipo":"agua", "nombre":"Haiti", "codigo":3}, 
    {"tipo":"agua", "nombre":"Venezuela", "codigo":4}, 
    {"tipo":"agua", "nombre":"Panama", "codigo":5}, 
    {"tipo":"agua", "nombre":"Japon", "codigo":6})
    
    aire = ({"tipo":"aire", "nombre":"Katrina", "codigo":7}, 
    {"tipo":"aire", "nombre":"Harvey", "codigo":8},
    {"tipo":"aire", "nombre":"Maria", "codigo":9}, 
    {"tipo":"aire", "nombre":"Sandy", "codigo":10}, 
    {"tipo":"aire", "nombre":"Irma", "codigo":11}, 
    {"tipo":"aire", "nombre":"Ike", "codigo":12})
    
    fuego = ({"tipo":"fuego", "nombre":"Boston", "codigo":13}, 
    {"tipo":"fuego", "nombre":"Londres", "codigo":14}, 
    {"tipo":"fuego", "nombre":"Roma", "codigo":15},
    {"tipo":"fuego", "nombre":"Chicago", "codigo":16},
    {"tipo":"fuego", "nombre":"Halifax", "codigo":17},
    {"tipo":"fuego", "nombre":"Tokio", "codigo":18})
    
    tierra = ({"tipo":"tierra", "nombre":"Valdivia", "codigo":19},
    {"tipo":"tierra", "nombre":"Sumatra", "codigo":20},
    {"tipo":"tierra", "nombre":"Kamchatka", "codigo":21},
    {"tipo":"tierra", "nombre":"Ecuador", "codigo": 22},
    {"tipo":"tierra", "nombre":"Colombia", "codigo":23},
    {"tipo":"tierra", "nombre":"Sumatra", "codigo":24})
    
    album_completo = [agua, aire, fuego, tierra]
    return album_completo

def objetos_cromo(album_completo): #llena la lista de objetos global que representa al album
    for i in range(len(album_completo)):
            for j in range(len(album_completo[i])):
                codigo  =   album_completo[i][j]["codigo"]
                nombre  =   album_completo[i][j]["nombre"]                
                tipo    =   album_completo[i][j]["tipo"]
                
                cromoClass = cromo(codigo, nombre, tipo)                                
                classAlbum.append(cromoClass)    

def visualizar_cromos():
    print("========================================================")            
    print("========================================================")            
    for i in range(len(classAlbum)):             
        codigo  =   classAlbum[i].codigo
        nombre  =   classAlbum[i].Nombre_cromo
        tipo    =   classAlbum[i].Tipo_de_cromo
        if tipo == _AGUA:
            print(f"🌊🌊🌊🌊🌊🌊")                
        elif tipo == _AIRE:
            print(f"🌀🌀🌀🌀🌀🌀")
        elif tipo == _FUEGO:
            print(f"🔥🔥🔥🔥🔥🔥")
        elif tipo == _TIERRA:
            print(f"🌋🌋🌋🌋🌋🌋")
                            
        print(f"Codigo: {codigo} Tipo: {tipo} Nombre: {nombre}\t||")
        if (i +1) %3 == 0:
            print("\n")
        if (i + 1) %6 == 0:
            print("\n")
    print("========================================================")            
    print("========================================================")

def comprar_cromos():
    #llama a la global de numero de compras
    global numero_compras    
    if len(cromos_usuario) == _TOTAL_CROMOS:
        print("========================================================")            
        print("🌊🌋🔥🌀     --     <<<-GANASTE->>>     --  🌊🌋🔥🌀")            
        print("========================================================")
    else:
        #generar randomicamente 3 numeros que corresponden a los cromos adquiridos
        lista_sobre_cromos = [] # los cromos que salieron en esta compra
        cromos_en_sobre = 3 # numero de cromos en el sobre    
            
        for i in range(cromos_en_sobre):
            cromo_nuevo = random.randint(1, _TOTAL_CROMOS)
            lista_sobre_cromos.append(cromo_nuevo)
                
        print("========================================================")            
        print("========================================================")
        print(f"Obtuviste los siguientes cromos!: ")
        
        #tamaño de arreglo de sobre comprado por si se desea cambiar el tamaño del sobre en el futuro
        for i in range(cromos_en_sobre):
            #setear el cromo para presentar obtenidos
            for j in range(len(classAlbum)):      
                if classAlbum[j].codigo == lista_sobre_cromos[i]:
                    cromo_obtenido = classAlbum[j]
                    print(f"Número: {cromo_obtenido.codigo} \tTipo: {cromo_obtenido.Tipo_de_cromo}\tNombre: {cromo_obtenido.Nombre_cromo}")
                    break
            
            #agregar cromo nuevo a la coleccion del usuario
            #recuerda que el aleatorio te da el código del cromo, no la posicion
            if cromos_usuario.count(cromo_obtenido.codigo) == 0:
                cromos_usuario.append(cromo_obtenido.codigo)
        #incrementa el numero de compras unicamente cuando sea compra efectiva
        numero_compras += 1
    
    print(f"Has comprado {numero_compras} sobres" )    
    #print("========================================================")            
    print("========================================================")
    
def porcentaje_cromos():
    agua = 0
    aire = 0
    fuego = 0
    tierra = 0
    _total_cromos_elemento = 6
    for i in range(len(cromos_usuario)):
        for j in range(len(classAlbum)):
            if cromos_usuario[i] == classAlbum[j].codigo:
                cromo_tipo = classAlbum[j]
                if cromo_tipo.Tipo_de_cromo == _AGUA:
                    agua += 1
                    break
                elif cromo_tipo.Tipo_de_cromo == _AIRE:
                    aire += 1
                    break
                elif cromo_tipo.Tipo_de_cromo == _FUEGO:
                    fuego += 1
                    break
                elif cromo_tipo.Tipo_de_cromo == _TIERRA:
                    tierra += 1
                    break                                       
                    
    porcentaje_agua     =   (agua * 100)/_total_cromos_elemento
    porcentaje_aire     =   (aire * 100)/_total_cromos_elemento
    porcentaje_fuego    =   (fuego * 100)/_total_cromos_elemento
    porcentaje_tierra   =   (tierra * 100)/_total_cromos_elemento    
    #print("========================================================")            
    print("========================================================")
    print(f"Tienes {agua} cromos de AGUA tu porcentaje es 🌊: {porcentaje_agua:.2f}")
    print(f"Tienes {aire} cromos de AIRE tu porcentaje es 🌀: {porcentaje_aire:.2f}")
    print(f"Tienes {fuego} cromos de FUEGO tu porcentaje es 🔥 ES: {porcentaje_fuego:.2f}")
    print(f"Tienes {tierra} cromos de TIERRA tu porcentaje es 🌋 ES: {porcentaje_tierra:.2f}")
    
    if len(cromos_usuario) == _TOTAL_CROMOS:
        print("======== FELICIDADES COMPLETASTE EL ALBUM ==============")            
    else:
        print("============ AUN TE FALTAN CROMOS POR CONSEGUIR ========")            
    #print("========================================================\n")
    print("========================================================")

def visualiza_cromos_usuario():
    if len(cromos_usuario) == 0:
        print("/------------------------------------------------------\\")            
        print("|============ AUN NO TIENES NINGUN CROMO ==============|")
        print("\\------------------------------------------------------/")
    else:
        print("\n========================================================")   
        for i in range(len(cromos_usuario)):
            cromo_ver = 0
            for j in range(len(classAlbum)):
                if cromos_usuario[i] == classAlbum[j].codigo :
                    cromo_ver = classAlbum[j]            
                    break
            
            tipo_cromo = cromo_ver.Tipo_de_cromo
            tipo_cromo_texto = ""
            if tipo_cromo == _AGUA:
                tipo_cromo_texto = "Tipo: Agua🌊"
            elif tipo_cromo == _AIRE:
                tipo_cromo_texto = "Tipo: Aire 🌀"
            elif tipo_cromo == _FUEGO:
                tipo_cromo_texto = "Tipo: Fuego 🔥"
            elif tipo_cromo == _TIERRA:
                tipo_cromo_texto = "Tipo: Tierra 🌋"
                
            print(f"Número Cromo: {cromo_ver.codigo} Tipo Cromo: {tipo_cromo_texto} Nombre Cromo: {cromo_ver.Nombre_cromo}")
        print("========================================================")
        print(f"Te faltan {(len(classAlbum) - len(cromos_usuario))} para completar el album")
    
def ver_album_completado():
    num = 1
    print("\n----------------------------------------------------------------------------------------------------------------")
    for i in range(4):        
        print(colors[i] + "|", end='\t')        
        for j in range(6):            
            if cromos_usuario.count(num) == 0:
                print(num, end='\t\t')
            else:
                print("-",num,"-", end='\t\t')            
            num += 1        
        #print("\n")
        print("|" + _RESET)
    print("\n----------------------------------------------------------------------------------------------------------------\n")
    if len(cromos_usuario) == 24:
        print(f"Gracias por jugar {usuario}! ♥️😎😎 GANASTE 😎😎♥️\n")

#inicio del programa
usuario = input("\n Hola! 😎 Dime tu nombre: ")
userInput = -1
numero_compras = 0

album_completo = generador_cromos() #Generamos los cromos
objetos_cromo(album_completo)       #llenamos la lista de objetos cromo

while userInput != 0:
    menu(usuario)
    try:
        userInput = int(input("Ingresa tu opción: "))
        print("\n")            
        if userInput == 1:
            #visualizar_cromos()
            visualiza_cromos_usuario()            
        elif userInput == 2:
            #comprar sobre cromos
            comprar_cromos()
            
        elif userInput == 3:
            #porcentaje de cromos que tiene el usuario
            porcentaje_cromos()
        elif userInput == 4:
            ver_album_completado()
        elif userInput == 0:
            continue
        else:
            print("\n☣️ --- Opción Inválida --- ☣️\n")
    except ValueError:
        print("\n☢️ --- Ingresa Números Positivos --- ☢️\n")
print(f"Gracias {usuario}! ♥️ Vuelve pronto ♥️\n")



    
    
    



