/*
Escribe un programa que solicite al usuario ingresar el número de kilómetros recorridos por su coche y el número de litros consumidos. 
El script debe mostrar el consumo de combustible por kilómetro.

Un problema matemático muy simple número de litros dividido por número de kilómetros.

input: km, litros
output: consumo en L / km
*/

console.log("--- Ejercicio 05 ---");

let km = Number(prompt("Ingresa los km:"));
let litros = Number(prompt("Ingresa los litros:"));
let consumo = litros / km;
console.log("km, L:", km, litros);
console.log("Consumo:", consumo);

document.write("<p>Para los datos km y L: " + km + " " + litros + "</p>");
document.write("<p>tenemos un consumo de: " + consumo + " L / km </p>");
