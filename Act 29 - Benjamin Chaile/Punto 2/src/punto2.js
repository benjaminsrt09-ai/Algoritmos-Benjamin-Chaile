/*Ejercicio 2: Carrito de Compras con Conteo de Productos
Enunciado: Crear un carrito de compras utilizando LocalStorage, que permita a los
usuarios agregar productos y muestre la cantidad total de productos en el carrito.
1. Los productos deben tener un botón para agregar al carrito.
2. Al agregar un producto, se debe mostrar el número total de productos en el
carrito, almacenándolo en LocalStorage.
3. Al recargar la página, el número total de productos debe recuperarse de
LocalStorage y mostrarse correctamente.*/

function actualizarConteo() {
  
    const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    document.getElementById("conteoCarrito").textContent = carrito.length;
}

function agregarProducto(event) {
    const idProducto = event.target.getAttribute("data-id");
    const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    
  
    carrito.push({ id: idProducto });
    
  
    localStorage.setItem("carrito", JSON.stringify(carrito));
    
    actualizarConteo();
}

document.addEventListener("DOMContentLoaded", () => {
    actualizarConteo(); 
    
    const botones = document.querySelectorAll(".btn-agregar");
    for (let i = 0; i < botones.length; i++) {
        botones[i].addEventListener("click", agregarProducto);
    }
});