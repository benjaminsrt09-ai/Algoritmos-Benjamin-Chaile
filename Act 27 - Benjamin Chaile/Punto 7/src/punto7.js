/*Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.*/

document.getElementById("boton").addEventListener("click", () => {
    let deportes = [];

    if (document.getElementById("futbol").checked) {
        deportes.push("Fútbol");
    }
    if (document.getElementById("basquet").checked) {
        deportes.push("Básquet");
    }
    if (document.getElementById("tenis").checked) {
        deportes.push("Tenis");
    }

    document.getElementById("resultado").value = deportes.join(", ");
});

