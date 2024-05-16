// Ejercicio 04

// Divisores de un número

/**
 * Un número es divisor de otro si al dividirlo entre el otro número el resultado es un número entero.
 */

let num = 15;

// posibles divisores de 15: 3, 5, 7, 10;

let dividirPorTres = 15 / 3;
let dividirPorCinco = 15 / 5;
let dividirPorSiete = 15 / 7;
let dividirPorDiez = 15 / 10;

console.group("Divisores de 15:");
console.log("Antes de redondear a enteros:");
console.log("Dividir 15 por 3:", dividirPorTres);
console.log("Dividir 15 por 5:", dividirPorCinco);
console.log("Dividir 15 por 7:", dividirPorSiete);
console.log("Dividir 15 por 10:", dividirPorDiez);

// Comprobamos cuál es una división exacta:
// Transformamos / redondeamos los números a enteros:
dividirPorTres = parseInt(dividirPorTres);
dividirPorCinco = parseInt(dividirPorCinco);
dividirPorSiete = parseInt(dividirPorSiete);
dividirPorDiez = parseInt(dividirPorDiez);

// Comprobamos los restos en cada caso:
// Si el resto es cero, entonces es un divisor
let restoTres = 15, restoCinco = 15, restoSiete = 15, restoDiez = 15;
restoTres -= dividirPorTres * 3;    // 15 - 15 = 0 -> es divisor
restoCinco -= dividirPorCinco * 5;  // 15 - 15 = 0 -> es divisor
restoSiete -= dividirPorSiete * 7;  // 15 - 14 = 1 -> no es divisor
restoDiez -= dividirPorDiez * 10; // 15 - 10 = 5 -> no es divisor

console.log("Conclusión:");
console.log("Resto de dividir 15 por 3:", restoTres, ", ¿3 es divisor?", restoTres === 0);
console.log("Resto de dividir 15 por 5:", restoCinco, ", ¿5 es divisor?", restoCinco === 0);
console.log("Resto de dividir 15 por 7:", restoSiete, ", ¿7 es divisor?", restoSiete === 0);
console.log("Resto de dividir 15 por 10:", restoDiez, ", ¿10 es divisor?", restoDiez === 0);
console.groupEnd();

// Conclusiones: los números 3 y  5 son divisores de 15. El 7 y el 10 no son divisores y por eso la comparacion es false.