/*
En una variable tienes el lado de un cuadrado, debes escribir un programa que te calcule el área y el perímetro del cuadrado.

El área la calculas como lado multiplicado por lado. 
El perímetro es la suma de los cuatro lados.

input: lado
outputs: perímetro, área

Ejemplo:

lado = 10
P = 40
A = 100

*/

let lado = 10;
let perimetro = 4 * lado;
let area = lado * lado;
console.log("--- Ejercicio 02 ---");
console.log("Lado:", lado);
console.log("Perímetro:", perimetro);
console.log("Área:", area);
// Escribimos la salida usando document.write():
document.write("<p>El lado es: " + lado + " u</p>");
document.write("<p>El perímetro es: " + perimetro + " u</p>")
document.write("<p>El área es: ", area + " u<sup>2</sup></p>");
