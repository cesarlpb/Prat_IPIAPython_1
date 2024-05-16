// Ejercicio 05

let res1 = 2 ** 3; // 8
let res2 = 2 ** 0; // 1
let res3 = 0 ** 0  // 1 -> https://es.wikipedia.org/wiki/Cero_elevado_a_cero

console.log("resultado 1:", res1); // 8
console.log("resultado 2:", res2); // 1
console.log("resultado 3:", res3); // 1 en JS

// Conclusión: el operador ** sirve para calcular potencias y en el caso de 0 ** 0 JS nos devuelve un 1 para evitar "problemas" con otros cálculos pero al ser la base 0 es una operación que puede causar confusiones.

// -> Se puede evitar verificando si la base es 0 y el exponente es 0, en cuyo caso se puede devolver NaN o un mensaje de error, etc.