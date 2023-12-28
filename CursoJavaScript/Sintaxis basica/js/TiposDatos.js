/* 


Tipos de Datos

PRIMITIVOS:
-String
-Number
-Boolean
-Null
-Undefined
-Symbols

REFERENCIADOS:
-Array
-Objetc
-Functions
-Dates


*/

const nombre = "Alejandro dijo: 'este curso esta makia' "
const nombre2 = 'Deivy'
//console.log(nombre , nombre2);

const amigos = 3;
const pi = 3.14159;
console.log(typeof(amigos) ,typeof(pi));

const isYoutuber = false;
console.log(isYoutuber , typeof isYoutuber); //Boolean

const felicidad = null;
console.log(felicidad , typeof felicidad); //Null

let novia;
console.log(novia , typeof novia); // No inicializado

const lenguajes = ["C++" , "JavaScript" , "C" , "Python"]
console.log(lenguajes, typeof lenguajes);

const video = {
    
    title: "Super video",
    likes: 52,
    subsGanados: 10,
};

console.log(video , typeof video);


//CAMBIOS DE DATOS 

let temperatura = 16.5;
console.log(temperatura , typeof temperatura);

temperatura = String(16.5);
console.log(temperatura, typeof temperatura);

let hora = 7
console.log(hora , typeof hora);

console.log(hora.toString , typeof hora.toString);

let valor = "30.4"
console.log(valor, typeof valor)

let valorNumerico = Number(valor)
console.log(valorNumerico , typeof valorNumerico);

let entero = parseInt(valor)
console.log(entero);