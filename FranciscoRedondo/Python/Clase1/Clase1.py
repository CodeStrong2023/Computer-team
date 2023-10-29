# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ["Naty","Osvlado", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) #solo muestra el indice que nosotros marquemos desde el 0 a 1.
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #con el espacio se da por entendido que empieza desde el indice 0 hacia delante
print(nombres[1: ]) #desde el indice uno hasta el final de la lista
#modificamos un valor dentro de nuestra lista
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar nuestra lista
for nombre in nombres:  # nombre es singular, la lista es plural 
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene una lista 
print(len(nombres)) #es una funcion que nos permite ver la cantidad de elemtnos que contiene una lista 

#Agregamos un elemento a nuestra lista
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)
#Se insertó el nombre a lo ultimo
nombres.insert(1,"Alberto") #Colocamos el nombre en un lugar en especifico, en este caso en el indice 1
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

#Eliminamos un elemento de la lista
nombres.remove("Alberto")
print(nombres)

#elimamos el ultimo elemento

nombres.pop()   #esta funcion usandola de esta manera lo que borra no es el ultimo elemento ingresado sino que borra el ultimo elemento de la lista
print(nombres)
#elimniar un indice espeífico
del nombres [2] #del signifca delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista
del nombres
print(nombres)

