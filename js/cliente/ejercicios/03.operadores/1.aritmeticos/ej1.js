// Ejercicio 01

// Operaciones combinadas

let op1 = 10 + 5 * 2;   // 10 + 10 = 20
let op2 = (10 + 5) * 2; // 15 * 2 = 30
let op3 = 10 + (5 * 2); // 10 + 10 = 20

console.log("operación 1:", op1); // 20
console.log("operación 2:", op2); // 30
console.log("operación 3:", op3); // 20

// Conclusión: los parentesis cambian la prioridad de las operaciones y nos varía el resultado en función de eso.

// Área del círculo

let r = 10;
const PI = 3.14;
let area = PI * r ** 2;

console.log("área:", area); // 314

// Conclusión: el operador ** es el operador de exponenciación, en este caso elevamos el radio al cuadrado.

// ¿Cómo podemos hacer un programa que reciba el radio r como dato y devuelva el área de la circunferencia? 

// -> Se puede hacer un programa que reciba el radio usando prompt y calcule el área del círculo.

/**
 * let r = Number(prompt('Ingrese el radio del círculo'));
 * ... resto del programa anterior ...
 */