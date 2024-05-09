/*
Cambio de unidades. En este ejercicio debes convertir a segundos 
una medida de tiempo dada en horas y minutos.

Recuerda una hora son 60 minutos y cada minuto son 60 segundos.

inputs: hora, minutos
output: segundos

Ejemplo:
1h 45min

1 * 3600 = 3600
45 * 60 = 2700
segundos = 6300 s

*/

console.log("--- Ejercicio 06 ---");

let dato = prompt("Introduce las horas:");
let horas = Number.parseInt(dato); // Convierte el texto a entero
dato = prompt("Introduce los minutos:");
let minutos = Number.parseInt(dato); // Convierte el texto a entero
console.log("h:m", horas, ":", minutos);

// Conversión a segundos:
let segundos = horas * 3600 + minutos * 60;
console.log("segundos:", segundos);


// Escribir en el documento HTML:
document.getElementById("ej-6-inputs").innerText = "hh:mm " + horas + ":" + minutos;
document.getElementById("ej-6-output").innerText = "segundos: " + segundos;