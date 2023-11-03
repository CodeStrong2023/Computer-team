#Ejercicio 7: juego adivina el numero
#Realizar un juego para adivinar un numero. Para ello se debe
#Generar un numero aleatorio entre 1 - 100, y luego ir pidiendo 
#numeros indicando "es mayor" o "es menor" segubn lo sea con respecto a N. El proceso
#terimna cuando el usuario acierta y allí se debe mostar el número de intentos
import random
print("\t. Esto es el juego Adivina el número")
aleatorio = random.randint(0,100) #toma numeros de 0 a 100
contador = 0
while True: 
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digita un número menor")
    elif numero < aleatorio:
        print("\tNo es el número, digite un número mayor")
    else: 
        print(f"Felicidades, acabas de adivinar el numero {aleatorio}")
        break #Rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")