#Ejercicio2: Función con * args para multiplicar 
#Crear una función para multiplicar los valores recibidos,
#utilizando argumentos variables *args
#Como parametro de la función y regresar como resultado
#la multiplicación de todos los valores pasados como argumentos

#Definimos la función para multiplicar

def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


#Llamamos a la función
print(multiplicar_valores(3, 5, 15, 3)) #Le pasamos los argumentos
