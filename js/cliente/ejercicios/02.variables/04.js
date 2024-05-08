/*
En este ejercicio vas a pedir al usuario que teclee tres números enteros y el script mostrará como resultado el valor medio de los tres.

Recuerda que la media de tres números se calcula sumando los tres y dividiendo entre 3.

inputs: num1, num2, num3 // enteros
output: promedio         // floats

Ejemplo:
inputs: 10, 20, 30
output: 60 / 3 = 20

*/

// Pedimos los tres números:
let num1 = Number(prompt("Introduce el primer número:"));
let num2 = Number(prompt("Introduce el segundo número:"));
let num3 = Number(prompt("Introduce el tercer número:"));

// Hacemos una conversión (casting) de String a Number

let promedio = ( num1 + num2 + num3 ) / 3;
alert("El promedio es: " + promedio);

// Probad números: 10, 20, 30
// Probad números: 0.1, 0.2, 0.3