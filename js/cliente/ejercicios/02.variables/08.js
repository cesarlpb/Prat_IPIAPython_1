/* 
Una tortilla de patatas lleva 200 gramos de patatas por persona. 
Por cada kilo de patatas se necesitan 5 huevos y 300 gramos de cebolla. 
Escribe un script que dado el número de comensales calcule las cantidades de ingredientes necesarias.

input: comensales
outputs: ingredientes -> gramosPatatas, gramosCebolla, huevos

2 comensales

2 * 200 gramos = 400 gramos de patatas
kgPatatas = gramosPatatas / 1000 -> float

huevos = kgPatatas * 5 -> int
0.4 * 5 = 2

gramosCebollas = 300 * kgPatatas
300 * 0.4 = 120 g

2 => 400, 2, 120

*/

console.log("--- Ejercicio 06 ---");

let comensales = Number.parseInt(prompt("Introduce el número de comensales:"));

// Constantes:
const GRAMOS_PATATAS_POR_PERSONA = 200;
const HUEVOS_POR_KG_PATATA = 5; // posible mejora: 7 - 9
const GRAMOS_CEBOLLA_TORTILLA = 300;

let gramosPatatas = GRAMOS_PATATAS_POR_PERSONA * comensales;
let kgPatatas = gramosPatatas / 1000;
let huevos = HUEVOS_POR_KG_PATATA * kgPatatas;
// Comprobamos los datos:
// console.log(gramosPatatas, kgPatatas, huevos);
huevos = Math.ceil(huevos);
// console.log(huevos)

let gramosCebolla = GRAMOS_CEBOLLA_TORTILLA * kgPatatas;
console.log(gramosPatatas, huevos, gramosCebolla)

// Escribimos salida:
let msg = `
  <p>Para ${comensales} comensales se necesitan:</p>
  <ul>
    <li>${gramosPatatas} g patatas</li>
    <li>${huevos} huevos</li>
    <li>${gramosCebolla} g cebolla</li>
  </ul>
`
document.getElementById("ej-8").innerHTML = msg;