/*2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados.*/

function mostrarVisita() {
    const nombre = document.getElementById('nombreVisita').value;
    const mail = document.getElementById('mailVisita').value;
    const comentarios = document.getElementById('comentariosVisita').value;
    
    alert("Nombre: " + nombre + "\nMail: " + mail + "\nComentarios: " + comentarios);
}