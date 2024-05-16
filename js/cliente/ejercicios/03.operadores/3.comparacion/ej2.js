// Ejercicio 02

let edad = Number(prompt("Ingrese su edad: "));

console.log("¿Es mayor de 18?", edad > 18);

console.log("¿Es menor de 18?", edad < 18);

console.log("¿Está entre 25 y 35 años?", edad >= 25 && edad <= 35);

console.log("¿No es mayor de 65 años?", !(edad > 65));

console.log("¿Tiene entre 13 y 24 años?", edad >= 13 && edad <= 24);

// Conclusión: a veces, se puede elegir entre cambiar el sentido de la comparación o negar el resultado de la comparación como en el caso de los 65 años. Elegid la forma más sencilla pero comprobad que funcion bien.
