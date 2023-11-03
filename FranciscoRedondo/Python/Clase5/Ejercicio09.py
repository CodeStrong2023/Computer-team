#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le devolverá
#la misma frase pero sin espacios en blanco, y ademas un contador de cuantos
#caracteres tiene la frase sin contar los espacios en blanco

frase1 = input("Escriba una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"Nª de caracteres: {len(frase1)}") #la funcion len nos muestra el numero de caracteres de una frase
