#Definimos una tupla 
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

#como podemos acceder a un elemento
print(cocina[0])
# mostar de manera inversa

print(cocina[-1])

#acceder a un rango 

print(cocina[0:2])
#Ejemplo 
verduras = ("papa",) #una tupla necesita siempre la coma aunque sea solo un elemento

#Recorremos los elemntos de la tupla 
for cocinar in cocina:
    print(cocinar, end= " ") #Usamos end para eliminar los saltos de linea


cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n",cocina)


del cocina 
print(cocina)
