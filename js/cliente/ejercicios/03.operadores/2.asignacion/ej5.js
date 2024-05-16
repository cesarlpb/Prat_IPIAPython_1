// Ejercicio 05

// Operaciones sobre una variable

let saldo = 100;
saldo *= 0.9; // 90% de 100 -> 90
// saldo = saldo * 0.9;
// etc.

saldo -= 15; // 90 - 15 -> 75
saldo *= (1 + 12.5 / 100); // 84...

saldo /= 2; // 42...
saldo *= (1 + 21 / 100); // 51...

console.log(saldo); // 51.046875

// Conclusión: hay que tener cuidado con las operaciones aritméticas + asignación como *= porque si ponemos otra operación adcicional puede hacer otro cálculo.
