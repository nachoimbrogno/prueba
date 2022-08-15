'''Primer módulo
Crear un módulo que tenga una clase con atributos y métodos. Instanciar a la clase llamando al módulo desde otro 
archivo .py.
Hacer una clase fácil, como Persona, con nombre y apellido, con un método hablar()
Crear una instancia de persona, mostrando sus datos y llamando al método desde otro módulo.
'''

#Importo los modulos de primer modulo (otr forma puede ser "from primer_modulo import Persona")
import primer_modulo

nom=input("Ingrese un nombre: ")
ape=input("Ingrese un apellido: ")

#Creo el objeto persona1 (si antes importe el modulo con "from primer_modulo import Persona" debo llamarlo persona1=Persona(...) )
persona1=primer_modulo.Persona(nom,ape)

persona1.hablar()