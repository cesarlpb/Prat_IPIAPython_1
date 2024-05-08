/*
Escribe un programa que solicite al usuario ingresar el número de kilómetros recorridos por su coche y el número de litros consumidos . El script debe mostrar el consumo de combustible por kilómetro.

Un problema matemático muy simple numero de litros dividido por número de kilómetros.

input: km, litros
output: consumo en L / km
*/

// Pedimos los datos:
let km = Number(prompt("Introduce los km recorridos:"));
let litros = Number(prompt("Introduce los litros gastados:"));

let consumo = litros / km;
alert("El consumo es de " + consumo + " L/km.")