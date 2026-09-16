/*Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)*/

document.getElementById("boton").addEventListener("click", () => {
    const preguntas = ["p1", "p2", "p3", "p4"];
    let correctas = 0;
    let incorrectas = 0;

    preguntas.forEach((id) => {
        const respuesta = document.getElementById(id).value;

        if (respuesta == "correcta") {
            correctas++;
        } else if (respuesta == "incorrecta") {
            incorrectas++;
        }
    });

    document.getElementById("correctas").value = correctas;
    document.getElementById("incorrectas").value = incorrectas;
});