/*

Un poco de interactividad. En este ejercicio debes escribir un programa que lea el nombre del usuario y salude con un "Hola" seguido del nombre del usuario.

Para leer el nombre usa un prompt con un texto indicativo como "Escribe tu nombre"

input: nombre -> "Pepe"
output: mensaje -> "Hola, Pepe"

*/

// Pedimos el nombre del usuario:
let nombre = prompt("¿Cómo te llamas?");
let mensaje = "Hola, " + nombre;
alert(mensaje); 
