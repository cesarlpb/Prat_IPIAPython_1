// Ejercicio 04

let str = "Hola, ¿qué tal?";

// Calculamos los caracteres del string:
let chars = str.length
console.log("¿Tiene más de 10 caracteres?", chars > 10);

// Método 1: usamos el método startsWith()
let empiezaPorH = str.startsWith("H");
console.log("¿Empieza por H?", empiezaPorH)

// Método 2: leer el primer caracter y compararlo con 'H'
let primerChar = str[0];
let primerChar2 = str.charAt(0)
console.log(primerChar, primerChar2)

console.log("¿Empieza por H?", primerChar == 'H');
console.log("¿Empieza por H?", primerChar2 == 'H');

// Miramos si tiene espacio (sabemos que sí) con el método includes():
let contieneEspacio = str.includes(" ");
console.log("¿Contiene espacio?", contieneEspacio);

// Colocamos la condición para verificar si es null o undefined y lo negamos para tener 'no (es null o undefined):'

let noEsNuloOUndefined = !(str == null && str == undefined);
console.log("¿No es nulo o undefined?", noEsNuloOUndefined);

// Verificar si tiene más de 5 chars:
let tieneMasDe5Chars = str.length > 5;
console.log("¿Tiene más de 5 chars?", tieneMasDe5Chars);