/*
En este ejercicio vas a pedir al usuario que teclee tres números enteros 
y el script mostrará como resultado el valor medio de los tres.

Recuerda que la media de tres números se calcula sumando los tres y dividiendo entre 3.

inputs: num1, num2, num3 // enteros
output: promedio         // floats

Ejemplo:
inputs: 10, 20, 30
output: 60 / 3 = 20

*/

console.log("--- Ejercicio 04 ---");

let num1 = Number(prompt("Ingresa el primer número:"));
let num2 = Number(prompt("Ingresa el segundo número:"));
let num3 = Number(prompt("Ingresa el tercero número:"));

let suma = num1 + num2 + num3;
console.log("Datos recibidos:", num1, num2, num3);
// Comprobamos la suma de los números recibidos:
console.log("Suma:", suma);
// Calculamos el promedio:
let promedio = suma / 3;
console.log("Promedio:", promedio);

// Escribimos los datos en el HTML:
document.getElementById("ej-4-inputs").innerText = "Números: " + num1 + ", " + num2 + ", " + num3;
document.getElementById("ej-4-output").innerText = "Promedio: " + promedio;

// Probad números: 10, 20, 30
// Probad números: 0.1, 0.2, 0.3