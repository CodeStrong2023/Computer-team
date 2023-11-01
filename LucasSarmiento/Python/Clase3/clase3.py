#Repaso de set o conjunto 
conjunto = set() #los conjuntos son grupos de elementos desordenados
conjunto1 = {"bye",}
conjunto.add(7)
conjunto.add("Hola")
print(conjunto)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el numero 3 no está en el conjunto1

#como hacer la igualdad de 2 conjuntos 
print(conjunto1 == conjunto)

#Operaciones en conjuntos
conjunto2 = conjunto | conjunto1 #la linea une los dos conjuntos
print (conjunto2)

conjunto2 = conjunto & conjunto1 #Que elementos tienen nen común
print(conjunto2)

conjunto2 = conjunto - conjunto1 #Asigna el valor que esta en el conjunto y no en el conjunto1
print(conjunto2)

conjunto2 = conjunto1 - conjunto
print(conjunto2)

conjunto2 = conjunto ^ conjunto1 # Son los elementos que están en los 2 conjuntos y no están compartidos
print(conjunto2)

# como hacer para que  un conjunto este dentro de otro conjunto 
conjunto2 = conjunto | conjunto1
print(conjunto1.issubset(conjunto2)) #Dentro del conjunto 3 se están guardando 2 conjuntos. Preguntamos si un conjunto está dentro de otro 
print(conjunto.issubset(conjunto2))
print(conjunto2.issubset(conjunto))
print(conjunto2.issubset(conjunto1))

print(conjunto2.issuperset(conjunto)) #preguntamos si los elementos del conjunto están dentro del 2 True
print(conjunto2.issubset(conjunto1)) #Preguntamos si los elementos del conjunto1 están dentro del 2 True
print(conjunto1.issubset(conjunto2))

#Como saber si ambos conjutnos son disconexos, esto es si no compraten elementos en comun 
print(conjunto.isdisjoint(conjunto1))

#convertir un conjunto totalmente en inmutable
conjunto = frozenset #esto hace que el conjunto sea totalmente inmutable, no se puede agregar ni modificar ni eliminar elementos del conjunto

#Repaso de diccionarios 
diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde" : "Green", "Amarillo": "Yellow"}
print(diccionarioNuevo)

#Como eliminar 
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)
#Los diccionarios pueden almacenar distintos tipos de datos 
diccinario2 = {"Ariel": {"Edad": 40, "Altura": 1.83}, "Osvaldo": [45, 1.85], "Natalia": [35, 1.67]}
print(diccinario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Ángel Dimaria", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Portero"},
    3: {"Nombre": "Nicolas Tagliafico", "Edad": 30, "Altura": 1.60, "Precio": "20 Millones", "Posicion": "Lateral"},
    9: {"Nombre": "Julian Alvarez", "Edad": 23, "Altura": 1.77, "Precio": "30 Millones", "Posicion": "Delantero"},
    23: {"Nombre": "Emiliano Martinez", "Edad": 33, "Altura": 1.90, "Precio": "25 Millones", "Posicion": "Portero"},
    13: {"Nombre": "Cuti Romero", "Edad": 25, "Altura": 1.73, "Precio": "20 Millones", "Posicion": "Defensa"},
   
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)


print("Tenemos cargados en el diccionario la cantidad de:  ", end=" ")
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final 

pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final 
elementoBorrado = pila.pop() #Quita el último elemento y lo guarda en la variable 
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora quedó así: {pila}")

#Colas con listas 
#Estructura de datos de tipo fifo(first input/first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

#Agregamos elementos al final de la cola

cola.append("Natalia")
cola.append("Jose")
print(cola)

#Sacamos elemetos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

