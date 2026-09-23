/*Ejercicio práctico #1:
Aplicar el consumo de API Fetch en tu proyecto personal
Enunciado: En este ejercicio, vas a integrar el consumo de una API REST utilizando
fetch() en tu proyecto personal de e-commerce o cualquier otro proyecto que estés
desarrollando. Los pasos a seguir son:
1. Elige una API pública (como Fake Store API) que te proporcione datos de
productos, usuarios y usuarias o cualquier otro recurso que quieras mostrar en
tu proyecto.
2. Usa fetch() para hacer una solicitud a la API y obtener los datos.
3. Muestra los datos obtenidos en tu proyecto, ya sea en forma de lista de
productos, usuarias o usuarios o lo que elijas.
4. Asegúrate de manejar los posibles errores utilizando .catch() y mostrá un
mensaje si algo falla.
5. Opcional: Integra los datos obtenidos con alguna funcionalidad de tu proyecto,
como un carrito de compras o una lista de productos favoritos.*/



const urlAPI = 'https://fakestoreapi.com/products';
const contenedorProductos = document.getElementById('grid-productos');
const contenedorError = document.getElementById('mensaje-error');

function obtenerDatos() {
    fetch(urlAPI)
        .then(respuesta => {
            if (!respuesta.ok) {
                throw new Error('No se pudo establecer conexión con la API');
            }
            return respuesta.json();
        })
        .then(productos => {
            mostrarProductos(productos);
        })
        .catch(error => {
            console.error('Detalle del error:', error);
            contenedorProductos.innerHTML = ''; 
            contenedorError.style.display = 'block';
            contenedorError.textContent = 'Hubo un problema al cargar el catálogo. Por favor, intenta de nuevo más tarde.';
        });
}

function mostrarProductos(productos) {
    contenedorProductos.innerHTML = ''; 

    productos.forEach(producto => {
        const tarjeta = document.createElement('div');
        tarjeta.className = 'tarjeta';
        
        tarjeta.innerHTML = `
            <img src="${producto.image}" alt="${producto.title}">
            <h3>${producto.title}</h3>
            <div class="precio">$${producto.price.toFixed(2)}</div>
            <button class="btn-favorito" onclick="alternarFavorito(this)">Añadir a favoritos</button>
        `;
        
        contenedorProductos.appendChild(tarjeta);
    });
}

function alternarFavorito(boton) {
    boton.classList.toggle('activo');
    
    if (boton.classList.contains('activo')) {
        boton.textContent = 'En favoritos';
    } else {
        boton.textContent = 'Añadir a favoritos';
    }
}

obtenerDatos();