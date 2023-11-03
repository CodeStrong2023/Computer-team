#Ejercicio 3: insertar elementos y ordenarlos
#Pedir números y meterlos en una lista, cuando el usuario
#introduzca un numero 0, nuestro programa dejaría de insertar.
#Por ultimo mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:  #el not cambia el valor de salir(false) a verdadero
    numero = int(input("Digite un número: "))
    if numero ==0:
        salir = True
    else: 
        lista.append(numero)
lista.sort() #la lista esta ordenada con esta función
print(f"\nLista ordenada: \n{lista}")

              