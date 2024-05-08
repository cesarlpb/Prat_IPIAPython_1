/*

Has hecho una compra y sabes el precio del producto y su iva. Haz un script que te calcule el precio total que vas a pagar por tu compra. 

Te recuerdo que para calcular el total debes sumar al precio el resultado de multiplicasr precio por el iva y dividir por 100.

input: precio, iva
output: total

Ejemplo:

input: 100, 21
output: 121

input: 200, 21
output: 242

*/

// Caso 1:
let precio = 100; // €
let iva = 21; // porcentaje
let impuesto = ( iva / 100 ) * precio; // 21 € 
let total = precio + impuesto;
console.log(precio, iva, "total:", total)

// Finalmente, escribimos el resultado en el id: ej-1-1
document.getElementById("ej-1-1").innerText = total;

// Caso 2:
precio = 200;
impuesto = ( iva / 100 ) * precio; // 42 €
total = precio + impuesto;
console.log(precio, iva, "total:", total)
// Finalmente, escribimos el resultado en el id: ej-1-2
document.getElementById("ej-1-2").innerText = total;