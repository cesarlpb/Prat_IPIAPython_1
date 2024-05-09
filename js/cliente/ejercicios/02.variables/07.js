/*
En este script debes pedir al usuario un número de dos dígitos y debes devolver el número de unidades y de decenas, o sea, cada dígito del número. Usa solo operationes aritméticas.

Recuerda si divides un número entre 10 el cociente entero es
el número de decenas y el resto es el número de unidades.

input: número de dos dígitos entre 10 y 99 -> entero
output: decenas, unidades -> enteros

Ejemplo:

54
d = 5
54 - 5 * 10 = 4
decenas -> 5
unidades -> 4

*/

console.log("--- Ejercicio 06 ---");

let num = Number.parseInt(prompt("Introduce un número entre 10 y 99:"));
let decenas = Number.parseInt(num / 10);
let unidades = Number.parseInt(num - decenas * 10);

console.log("D U", decenas, unidades);

// Escribimos en el documento:
document.getElementById("ej-7").innerText = `El número ${num} tiene ${decenas} decenas y ${unidades} unidades.`
