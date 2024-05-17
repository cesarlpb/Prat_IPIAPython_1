// Ejercicio 04

// Concatenamos dos <p> de HTML como strings:
let p1 = "<p>Esto es un párrafo</p>";
let p2 = "<p>Esto es otro párrafo</p>";
let res = p1 + " " + p2;

// Estas cadenas que tienen HTML se pueden introducir como innerHTML dentro de un elemento del documento con JS

// Creamos un div con una lista:
let div = "<div>\n";
let lista = "<ul>\n";
let li = "<li>Elemento 1</li>\n";
lista += li;
let li2 = "<li>Elemento 2</li>\n";
lista += li2;
let li3 = "<li>Elemento 3</li>\n";
lista += li3;
lista += "</ul>\n";
div += lista;
div += "</div>";

// Coloco esto en el container:
document.getElementById("container").innerHTML = div;

// Añadimos enlaces a los lis:
// Creamos un div con una lista:
let div2 = "<div>\n";
let lista2 = "<ul>\n";
let li4 = "<li><a href='#'>Elemento 1</a></li>\n";
lista2 += li4;
let li5 = "<li><a href='#'>Elemento 2</a></li>\n";
lista += li5;
let li6 = "<li><a href='#'>Elemento 3</a></li>\n";
lista2 += li6;
lista2 += "</ul>\n";
div2 += lista2;
div2 += "</div>";

// Coloco esto en el container:
document.getElementById("container2").innerHTML = div2;

// Conclusión: podemos generar HTML como string en JS y pasarlo a un elemento usando innerHTML y el navegador se encarga de interpretarlo como HTML de forma correcta.