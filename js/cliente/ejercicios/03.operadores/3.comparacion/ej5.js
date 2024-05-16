// Ejercicio 05

// Pedimos el día al usuario:
let dia = prompt("Introduce un día de la semana en minúsculas:");

// lunes, ..., viernes
const diasLaborables = [
  "lunes", "martes", "miércoles", "jueves", "viernes"
]
let esDiaLaborable = diasLaborables.includes(dia.toLowerCase()); // pasamos el dia a minúsculas
console.log("¿Es día laborable?", esDiaLaborable);

let esFinDeSemana = !esDiaLaborable; // exceptuando festivos

console.log("¿Es fin de semana?", esFinDeSemana)

let esLunesOJueves = dia.toLowerCase() == 'lunes' || dia.toLowerCase() == 'jueves';
console.log("¿Es lunes o jueves?", esLunesOJueves);

let esViernes = dia.toLowerCase() == 'viernes'
console.log("¿Es viernes?", esViernes);

let esNoLectivo = dia.toLowerCase() == 'martes'
console.log("¿Es no lectivo?", esNoLectivo);