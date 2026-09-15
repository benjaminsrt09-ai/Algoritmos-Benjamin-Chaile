/*Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
Si hay un empate, debe mostrar el mensaje “Hay un empate”.*/

let votosCandidato1 = 0;
let votosCandidato2 = 0;
let votosCandidato3 = 0;

let botonCandidato1 = document.getElementById("botonCandidato1");
let botonCandidato2 = document.getElementById("botonCandidato2");
let botonCandidato3 = document.getElementById("botonCandidato3");

let votosCandidato1Texto = document.getElementById("votosCandidato1");
let votosCandidato2Texto = document.getElementById("votosCandidato2");
let votosCandidato3Texto = document.getElementById("votosCandidato3");

function calcularGanador() {
    if (votosCandidato1 > votosCandidato2 && votosCandidato1 > votosCandidato3) {
        console.log("Va ganando el Candidato 1");
    } else if (votosCandidato2 > votosCandidato1 && votosCandidato2 > votosCandidato3) {
        console.log("Va ganando el Candidato 2");
    } else if (votosCandidato3 > votosCandidato1 && votosCandidato3 > votosCandidato2) {
        console.log("Va ganando el Candidato 3");
    } else {
        console.log("Hay un empate");
    }
}

botonCandidato1.addEventListener("click", function() {
    votosCandidato1 = votosCandidato1 + 1;
    votosCandidato1Texto.textContent = "Votos Candidato 1: " + votosCandidato1;
    calcularGanador();
});

botonCandidato2.addEventListener("click", function() {
    votosCandidato2 = votosCandidato2 + 1;
    votosCandidato2Texto.textContent = "Votos Candidato 2: " + votosCandidato2;
    calcularGanador();
});

botonCandidato3.addEventListener("click", function() {
    votosCandidato3 = votosCandidato3 + 1;
    votosCandidato3Texto.textContent = "Votos Candidato 3: " + votosCandidato3;
    calcularGanador();
});