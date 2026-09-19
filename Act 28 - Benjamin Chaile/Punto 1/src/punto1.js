/*1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no.*/


function verificarIngreso() {
    if (document.getElementById("mayor").checked) {
        alert("Puede ingresar al sitio.");
    } else if (document.getElementById('menor').checked) {
        alert("No puede ingresar al sitio.");
    } else {
        alert("Seleccione una opción.");
    }
}