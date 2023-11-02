// Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios 
es muy similar a la de Java
realmente diriamos que es identica
*/

var nombre = "Francisco";//Tipo string o Str
console.log(typeof nombre); 
nombre = 7
console.log(typeof nombre); 
nombre = 12.3
console.log(typeof nombre);

var numero = 3000; //Tipo Numerico
console.log(numero);

var objeto = {
    nombre : "Francisco",
    apellido : "Redondo",
    telefono : "2604414830"
}

console.log(typeof objeto); 

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion (nos permite reutilizar lineas de codigo)
function miFuncion(){}
console.log(typeof miFuncion); 

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof undefined);

//Tipo de dato null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es

var z = '';
console.log(z); //Esto se refiere a que es una cadena vacia
console.log(typeof z);

