#Ejercicio 3: funcion recursiva
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir: 
#5
#4
#3
#2
#1
#So se ingresan mumeros negativos no imprime nada
numeroIngresado = int(input("Digite un número: "))
def imprimir_numeros_recursivos(numero):
    if numero >= 1: 
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimir_numeros_recursivos(numeroIngresado)