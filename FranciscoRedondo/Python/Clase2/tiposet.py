# tipo set
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) #Usamos la función le = length significado largo

#revisar si un elemento existe dentro de set
print("Jupiter" in planetas)

#Agregar un elemento

planetas.add("Tierra") #add sirve para añadir elementos 
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe

planetas.remove("Jupiter") #esta función da error si el elemento no existe
print(planetas)
planetas.discard("Tierra") #Si el elemento ingresado no existe, no hace nada y tampcoo larga error
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

del planetas
#print(planetas) #al eliminar nos va a mostrar error porque ya no existe

#Diccionario en python (coleccion de datos u elementos)
# "Maradona" :10 un diccionario está compuesto por dos elementos una llave y un valor
# dict(key, value)
diccionario = {
    "IDE" : "Integrated Development Environment",
    "POO" : "Programación Orientada a Objetos",
    "SABD": "Sistemas de Administración de Base de Datos"
}
print(len(diccionario)) #la ¡funcion len nos muestra la cantidad de elemntos en vez de mostrar los nombres de cada uno de ellos 
print(diccionario)

#Acceder a uun diccionario con la llave
print(diccionario["IDE"])

#Recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#modificar los elementos 
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

#Como recorrer los elementos 
for termino in diccionario: #Recorremos solo mostrando las llaves
    print(termino)

#Necesitamos una funcion para reccorrer un diccionario en tanto la llave como el valor 
for termino, valor in diccionario.items(): 
    print(termino,valor)


#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #muestra solo las llaves

for valor in diccionario.values(): #nos muestra los valores pero sin las llaves
    print(valor)
#comprobar la existencia de algun elemento
print("IDE" in diccionario)

#Agregamos un elemento 
diccionario["PK"] = "Primary Key"
print(diccionario)

#eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario

diccionario.clear()
print(diccionario)

#Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9]) #Función para agregar varios elemntos a una lista
print(lista3)

print(lista3.index(5)) #función para indicar en que indice esta el valor ingresado
#print(lista3.index(0)) #esto da error porque el 0 no es un elemento de la lista

#como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) 

#para poner al reves una lista
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elemetos 
lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento
lista3.sort() #ordena los elementos de manera ascendente 
print(lista3)

lista3.sort(reverse=True)
print(lista3)

#las tuplas son listas inmutables, puede tener distintos tipos de datos dentro
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola" )
print(tupla)

print(4 in tupla)