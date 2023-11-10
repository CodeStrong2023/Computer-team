# Ejercicio 8: Menú interactivo - Cajero automático
#Hacer un programa que simule un cajero automático con un saldo
#inicial de 1000$ y tendrá el siguiente menú de opciones:
            #1. Ingresar dinero de la cuenta
            #2. Retirar dinero de la cuenta
            #3. Mostrar dinero dispònible
            #4. Salir
saldo = 1000
while True:
    print("\t. :MENÚ:.")
    print("1. Ingresar dinero de la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero dispònible")
    print("4. Salir")
    opcion = int(input("Digite una opción de menú: "))
    print()
    if opcion == 1: 
        extra = float(input("Cuanto dinero desea ingresar ->"))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2: 
        retirar = float(input("Cuanto dinero desea retirar ->"))
        if retirar > saldo: 
            print("No tiene dinero suficiente")
        else: 
            saldo -= retirar
            print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 3: 
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 4: 
        print("Gracias por utilizar su cajero automático, hasta pronto")
        break
    else: 
        print("Error, se equivocó de opción de menú)")
        print()

