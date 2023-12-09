class hijo:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def __str__(self):
    return f"{self.nombre}({self.edad})"
  
  def saludo(self):
    print("Hola mi nombre es: " + self.nombre)
  
  
ruben = hijo("Ruben", 3)

ruben.saludo()

print(ruben)

ruben.edad = 44

print(ruben)

