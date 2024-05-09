/*

Un poco de interactividad. En este ejercicio debes escribir 
un programa que lea el nombre del usuario y salude con un 
"Hola" seguido del nombre del usuario.

Para leer el nombre usa un prompt() con un texto indicativo 
como "Escribe tu nombre"

input: nombre -> "Pepe"
output: mensaje -> "Hola, Pepe"

*/

console.log("--- Ejercicio 03 ---");
console.log("Responde al prompt() y verás un alert() con un saludo :)")
// Pedimos el nombre del usuario:
let nombre = prompt("¿Cómo te llamas?");
let saludo = "Hola, " + nombre;
alert(saludo); 
