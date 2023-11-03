class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostar_detalle(self):
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.edad} {self. apellido},{self._dni}la dirección es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Ariel", "Betancud", 32456987, 40)        
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es {persona1.edad}")
      
persona2 = Persona("Osvaldo", "Giordanini", 30321456, 45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es {persona1.edad}")

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostar_detalle()
persona2.mostar_detalle()

#Persona.mostar_detalle() #Debemos pasarle una referencia para el self o dará error 
persona1.telefono = "44445555289"
print(f"Este es el telefono: {persona1.nombre} {persona1.telefono}")
persona3 = Persona("Rogelio", "Romero",35789456, 22, "Teléfono", "2614445557", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito= "Azul", Auto="Citroen", Modelo=2021)
persona3.mostar_detalle()
