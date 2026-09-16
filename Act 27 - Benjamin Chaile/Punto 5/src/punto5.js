/*Generar un presupuesto de un equipo de computación a partir de tres
objetos de tipo SELECT que nos permiten seleccionar:
Procesador (Intel I3 - $400, Intel I5 $600, Intel I7 $800).
Monitor (Samsung 20&#39; - $250, Samsung 22&#39; - $350, Samsung 26&#39; - $550)
Disco Duro(500 Gb - $300, 1 Tb - $440, 3 Tb - $500)
Para cada característica indicamos string a mostrar (Ej. Intel I3) y el
valor asociado a dicho string (Ej. 400).
Al presionar un botón &quot;Calcular&quot; mostrar el presupuesto en un objeto de
tipo TEXT.*/

document.getElementById("boton").addEventListener("click", () => {
    const procesador = document.getElementById("procesador").value;
    const monitor = document.getElementById("monitor").value;
    const disco = document.getElementById("disco").value;

    const total = Number(procesador) + Number(monitor) + Number(disco);

    document.getElementById("presupuesto").value = "$" + total;
});