// Ejercicio 02

// Calculamos la longitud de estas cadenas:
console.log(`"" tiene longitud:`, "".length);
console.log("\"Hola\" tiene longitud:", "Hola".length);
console.log("\"1+1=2\" tiene longitud:", "1+1=2".length);

// Bloque no modificado:
const diasDeLaSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const diaDeLaSemana = diasDeLaSemana[new Date().getDay()];
// final de bloque no modificado

// Cadena:
let msj = "Hoy es " + diaDeLaSemana;
console.log("La longitud del msj es:", msj.length);

// Conclusión: las cadenas iniciales son fijas y por lo tanto su longitud siempre devuelve lo mismo. En cambio, la cadena final depende del día de la semana y por lo tanto el resultado de su longitud varía.