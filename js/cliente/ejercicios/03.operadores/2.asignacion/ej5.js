// Ejercicio 05

console.groupCollapsed('Ejercicio 05');

// Operaciones sobre una variable
// Valor inicial de 100:
let saldo = 100;

// Quitar 10%:
saldo *= 0.9; // 90% de 100 -> 90
// saldo = saldo * 0.9;
// etc.

// Restar 15:
saldo -= 15; // 90 - 15 -> 75

// Añadir 12.5%:
saldo *= (1 + 12.5 / 100); // 84...

// Dividir por 2:
saldo /= 2; // 42...

// Añadir 21%:
saldo *= (1 + 21 / 100); // 51...

console.log(saldo); // 51.046875
console.groupEnd();

// Conclusión: hay que tener cuidado con las operaciones aritméticas + asignación como *= porque si ponemos otra operación adcicional puede hacer otro cálculo.
