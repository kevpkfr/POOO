class persona:
    nombre = str
    apellido = str
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre, self.apellido)    
        
x = persona("Alexander", "Flores")        
x.imprimir()

class estudiante(persona):
    pass

y = estudiante("Jeremi", "Cañizares")
y.imprimir()

