#Crear una función para sumar los valores recibidos de tipo numéricos
#utilizando argumentos variables *args como parametro de la 
#función y agregar como resultado la suma de todos los valores pasados
#como argumentos.
#Definimos una función

def suma_valor(*args): #Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

#Llamamos a la funcion
print(suma_valor(3, 5, 9, 2, 1))