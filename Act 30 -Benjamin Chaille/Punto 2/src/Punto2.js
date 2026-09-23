/*Ejercicio práctico #2:
Crear un carrito de compras dinámico con productos de una API
Enunciado: Vas a crear un carrito de compras dinámico que permite agregar
productos al carrito utilizando datos obtenidos de una API externa. Los pasos
específicos son:
1. Utilizá fetch() para obtener una lista de productos desde una API (puede ser la
misma API de productos del Ejercicio 1).
2. Mostrá los productos en la página en forma de tarjetas o lista.
3. Agregá un botón &quot;Añadir al carrito&quot; para cada producto. Al hacer clic en el
botón, el producto debe añadirse al carrito.
4. Usá LocalStorage para almacenar los productos que se agreguen al carrito,
de manera que si recarga la página, los productos sigan allí.
5. Mostrá la cantidad de productos que hay en el carrito en todo momento,
actualizándose cada vez que se añada un nuevo producto. */



const urlAPI = 'https://fakestoreapi.com/products';
const contenedorProductos = document.getElementById('grid-productos');
const contenedorError = document.getElementById('mensaje-error');

document.addEventListener('DOMContentLoaded', () => {
    actualizarContador();
    obtenerDatos();
});

function obtenerDatos() {
    fetch(urlAPI)
        .then(respuesta => {
            if (!respuesta.ok) {
                throw new Error('Error al conectar con la API');
            }
            return respuesta.json();
        })
        .then(productos => {
            mostrarProductos(productos);
        })
        .catch(error => {
            contenedorProductos.innerHTML = '';
            contenedorError.style.display = 'block';
            contenedorError.textContent = 'Hubo un error al cargar los productos.';
        });
}

function mostrarProductos(productos) {
    contenedorProductos.innerHTML = '';

    productos.forEach(producto => {
        const tarjeta = document.createElement('div');
        tarjeta.className = 'tarjeta';
        
        tarjeta.innerHTML = `
            <img src="${producto.image}" alt="">
            <h3>${producto.title}</h3>
            <div class="precio">$${producto.price.toFixed(2)}</div>
            <button class="btn-agregar" onclick="agregarAlCarrito(${producto.id}, '${producto.title.replace(/'/g, "\\'")}', ${producto.price})">Añadir al carrito</button>
        `;
        
        contenedorProductos.appendChild(tarjeta);
    });
}

function agregarAlCarrito(id, titulo, precio) {
    let carrito = JSON.parse(localStorage.getItem('carrito_compras')) || [];
    
    carrito.push({ id, titulo, precio });
    
    localStorage.setItem('carrito_compras', JSON.stringify(carrito));
    
    actualizarContador();
}

function actualizarContador() {
    const carrito = JSON.parse(localStorage.getItem('carrito_compras')) || [];
    document.getElementById('contador-carrito').textContent = carrito.length;
}