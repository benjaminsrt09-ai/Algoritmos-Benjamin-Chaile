/*Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.*/

document.getElementById("pizza").addEventListener("change", () =>{
let select = document.getElementById("pizza");
let precio = select.value;

document.getElementById("precio").value = precio =="0" ? " " : "$" + precio;
})