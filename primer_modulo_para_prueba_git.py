'''Primer módulo
Crear un módulo que tenga una clase con atributos y métodos. Instanciar a la clase llamando al módulo desde otro 
archivo .py.
Hacer una clase fácil, como Persona, con nombre y apellido, con un método hablar()
Crear una instancia de persona, mostrando sus datos y llamando al método desde otro módulo.
'''

class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def hablar(self):
        print (f"Hola soy {self.nombre} {self.apellido} y estoy hablando.")