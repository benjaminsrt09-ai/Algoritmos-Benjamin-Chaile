/*Ejercicio 04: Lista de Compras Dinámica

Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (verificar)).
Además:
La lista debe permitir eliminar un producto haciendo clic sobre él.
En consola debe mostrarse en todo momento la cantidad de productos
actuales en la lista.*/

let boton = document.getElementById("boton");
let producto = document.getElementById("producto");
let lista = document.getElementById("lista");

boton.addEventListener("click", function() {

    if (producto.value != "") {

        let nuevo = document.createElement("li");

        nuevo.textContent = producto.value;

        lista.appendChild(nuevo);

        nuevo.addEventListener("click", function() {
            nuevo.remove();

            console.log("Cantidad de productos: " + lista.children.length);
        });

        producto.value = "";

        console.log("Cantidad de productos: " + lista.children.length);
    }

});