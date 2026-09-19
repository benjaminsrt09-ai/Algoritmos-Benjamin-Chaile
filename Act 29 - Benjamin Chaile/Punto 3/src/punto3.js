/*Ejercicio 3: Borrador de Notas de Sesión
Enunciado: Crear una aplicación de notas rápidas que permita al usuario escribir un
mensaje o nota en un campo de texto y guardarlo de forma temporal utilizando
SessionStorage.
 Debe contar con un campo de texto (&lt;textarea&gt; o &lt;input&gt;) y un botón &quot;Guardar
Nota&quot;.
 Al hacer clic en el botón &quot;Guardar Nota&quot;, el texto ingresado debe almacenarse
en SessionStorage y mostrarse en un elemento dentro del DOM (por ejemplo,
en un contenedor &lt;div&gt; o párrafo).
 Al recargar la página (F5), la nota guardada debe recuperarse de
SessionStorage y seguir mostrándose en pantalla.
 Debe incluir un botón &quot;Borrar Nota&quot; que elimine el registro de SessionStorage
mediante removeItem() y limpie el contenido del DOM.*/

function guardarNota() {
    const textoNota = document.getElementById("nota").value;

    sessionStorage.setItem("notaSesion", textoNota);
    mostrarNota();
}

function borrarNota() {

    sessionStorage.removeItem("notaSesion");
    

    document.getElementById("nota").value = '';
    mostrarNota();
}

function mostrarNota() {

    const notaGuardada = sessionStorage.getItem("notaSesion");
    const contenedor = document.getElementById("contenedorNota");
    
    if (notaGuardada) {
        contenedor.textContent = notaGuardada;
    } else {
        contenedor.textContent = "No hay notas guardadas.";
    }
}

document.addEventListener("DOMContentLoaded", mostrarNota);