#Una función siempre necesita ser llamdada para que se ejecute el codigo que está dentro de ese bloque
#Comenzamos con Funciones
#Definimos una función
# mi_funcion() #no se puede llamar antes de definir una función

def mi_funcion(): #Para identificar la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() #Estamos llamando a la funcion 
mi_funcion()
mi_funcion()

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función
show(*person) #Est0 es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvlado", "Giordanini") #Desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print("Esto se termina")

# list Comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# la palabra return en funciones
#Creamos una función para sumar 
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

#Valores por default
def sumar2(a: int = 0, b: int = 0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

#Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres: 
        print(nombre)
listarNombres("Lucas", "José", "Claudia", "Rosa", "María")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

def listarTerminos(**terminos): #lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa: key word argument
        print(f"{llave} : {valor}")

listarTerminos() #no recibe nada, nada se va a mostrar
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primaruy Key")
listarTerminos(Nombre="Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
desplegarNombres((10, 11)) #la convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) #La convertimos en una lista

#Funciones recursivas
def factorial(numero):
    if numero == 1: #Caso base
        return 1
    else:
        return numero * factorial(numero-1) #caso recursivo
numeroFactorial = int(input("Digite un número: "))
resultado = factorial(numeroFactorial) #lo hacemos en codigo duro
print(f"El factorial del numero ingresado es: {resultado}")
