var nombre = 'Francisco';
var apellido = ' Redondo;'
var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Lucas'+' '+ 'Sarmiento';
console.log(nombreCompleto2);
var juntos = nombre +' '+ 219; //Lee de izquierda a derecha siguiendo la cadena lee el numero como String
console.log(juntos);
juntos = nombre + 78 + 17; //Aqui se puede diferencias a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre; 
console.log(juntos);

nombre += apellido;
console.log(nombre);

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Perez";
//apellido2 = "Gonzalez"; es una constante que no puede ser modificada
console.log(apellido2);

let x, y;  //Se pueden crear varias variables dentro de una misma linea
x = 17, y = 21; //Se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y; //Se asigna el valor de la operacion
console.log(z);

let _1num = 31; //No utilizar numero para inciar el nombre de una variable
let rompiendo = "rompe"; //No utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);