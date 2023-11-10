#Ejercicio 1: Llenar una lista +
#Llenar una lista con los números del 1 al 50, luego mostrar
#la lista con el bucle for, los elementos deben mostrarse de la 
#Siguiente forma: 
# 1-2-3-4-5....-50

#lista = []
#i = 1
#while i <= 50:
#    lista. append(i)     #Todo esto se puede hacer en una sola linea de codigo
#    i += 1
lista = list(range(1,51)) #algoritmos eficaz
for i in lista:
    print(i,end="-")
