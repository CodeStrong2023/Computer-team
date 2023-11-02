//Ejercicio 1: Calcular estacion del año

let mes = 4;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);

//Ejercicio 2: Hora del dia

/*
De 6 a 11 nos saluda: Good Morning
De 12 a 16 nos saluda: Good Afternoon
De 17 a 19 nos saluda: Good Evening
De 20 a 23 horas nos saluda: Good Night
Trabajaremos con 24 horas
*/

let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <=11){
    mensaje = "Good Morning"
}
else if(horaDia >= 12 && horaDia <=16){
    mensaje = "Good Afternoon"
}
else if(horaDia >= 17 && horaDia <=19){
    mensaje = "Good Evening"
}
else if(horaDia >= 20 && horaDia <=23){
    mensaje = "Good Night"
}
else{
    mensaje = "Valor incorrecto";
}

console.log(mensaje);

//Estructura switch (la sintaxis es igual a Java)
switch(mes){ //No solo se pueden utilizar numeros, tambien cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estacion de: "+estacion);





//Ampliando el uso de var, let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
}
//console.log(nombre); //Aqui no lee el dato en la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo

/*
Let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2); 

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
Const: se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003; 
//console.log(fechaNacimiento); //Solo se ejecuta el console anterior

