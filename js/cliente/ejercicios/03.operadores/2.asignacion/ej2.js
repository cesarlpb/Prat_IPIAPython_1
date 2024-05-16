// Ejercicio 02

console.group("Ejercicio 02");
console.group("Solución sin operador de asignación");
let total = 50;
// Restamos 10
total = total - 10;
// Calculamos el 21% y lo sumamos
let porcentaje = total * 0.21;
total = total + porcentaje;
// Añadimos 20
total = total + 20;
// Calculamos 10% de 20 y lo sumamos
porcentaje = 20 * 0.1;
total = total + porcentaje;

console.log("Total:", total);
console.groupEnd(); // Cierra la parte de sin operador de asignación

console.groupCollapsed("Solución con operador de asignación");
// Valor inicial
total = 50;
console.log("Total inicial:", total);

total -= 10; // total = total - 10 -> 40
console.log("Restamos 10:", total);

// Sumamos el 21% sobre el total actual:
total += total * 0.21; // total = total + total * 0.21 -> 48.4
console.log("Sumamos el 21%:", total);

// Añadimos 20:
total += 20; // total = total + 20 -> 68.4
console.log("Añadimos 20:", total);

// Añadimos el 10% de 20:
total += 20 * 0.1; // total = total + 20 * 0.1 -> 70.4
console.log("Añadimos el 10% de 20:", total);

console.groupEnd(); // Cierra la parte de operadores de asignación
console.groupEnd(); // Cierra Ejercicio 02

// Conclusión: el paso en el que decidimos añadir el 21% del total actual también podría ser añadir el 21% de la total incial (50 de base) -> esto cambia el resultado según cual sea el supuesto / requerimiento del problema.

// Tip: si fuese un problema real, habría que aclarar este punto con el cliente o el responsable del proyecto.