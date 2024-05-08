/*
En una variable tienes el lado de un cuadrado, debes escribir un programa que te calcule el área y el perímetro del cuadrado.

El area la calculas como lado multiplicado por lado. El perímetro es la suma de los cuatro lados.

input: lado
outputs: perímetro, área

Ejemplo:

lado = 10
P = 40
A = 100

*/

let lado = 25;
// perímetro = 4 * lado
let P = 4 * lado;
// área = lado * lado
let A = lado * lado;

document.write("<p>El perímetro es: ", P, " u", "</p>");
document.write("<p>El área es: ", A, " u<sup>2</sup>", "</p>");