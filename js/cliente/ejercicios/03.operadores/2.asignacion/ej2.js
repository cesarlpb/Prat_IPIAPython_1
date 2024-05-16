// Ejercicio 02

let total = 50;
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

// Conclusión: el paso en el que decidimos añadir el 21% del total actual también podría ser añadir el 21% de la total incial (50 de base) -> esto cambia el resultado según cual sea el supuesto / requerimiento del problema.

// Tip: si fuese un problema real, habría que aclarar este punto con el cliente o el responsable del proyecto.