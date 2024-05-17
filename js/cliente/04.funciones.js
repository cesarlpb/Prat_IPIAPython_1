// Funciones

let numero = 0;
console.log("antes:", numero); // 0
function sumarUno(){
    numero = numero + 1;
    console.log("dentro:", numero) // 1
}
sumarUno();
console.log("después:", numero) // 1