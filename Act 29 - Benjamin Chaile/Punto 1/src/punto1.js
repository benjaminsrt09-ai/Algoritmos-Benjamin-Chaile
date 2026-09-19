/*Ejercicio 1: Guardar Preferencias de Usuario
Enunciado: Crear una función que guarde y recupere las preferencias de un usuario,
como su nombre y el color de fondo preferido, utilizando LocalStorage.
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente (mostrar el nombre del usuario y
cambiar el color de fondo).*/

function guardarPreferencias() {
    const nombre = document.getElementById("nombreUsuario").value;
    const color = document.getElementById("colorFondo").value;

    localStorage.setItem("nombre", nombre);
    localStorage.setItem("color", color);

    aplicarPreferencias();
}

function aplicarPreferencias() {

    const nombreGuardado = localStorage.getItem("nombre");
    const colorGuardado = localStorage.getItem("color");

    if (nombreGuardado) {
        document.getElementById("saludoUsuario").textContent = "¡Hola, " + nombreGuardado + "!";
    }
    if (colorGuardado) {
        document.body.style.backgroundColor = colorGuardado;
        document.getElementById("colorFondo").value = colorGuardado;
    }
}


document.addEventListener("DOMContentLoaded", aplicarPreferencias);