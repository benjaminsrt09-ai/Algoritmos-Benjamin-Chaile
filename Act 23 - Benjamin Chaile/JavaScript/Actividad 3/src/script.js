/*
Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8).
 */

function ordenar_tabla(nombres, puntos, diferencia) {
  let cantidad = nombres.length;

  for (let vuelta = 0; vuelta < cantidad - 1; vuelta++) {
    for (let posicion = 0; posicion < cantidad - 1 - vuelta; posicion++) {
      let cambiar = false;

      if (puntos[posicion] < puntos[posicion + 1]) {
        cambiar = true;
      } else if (puntos[posicion] === puntos[posicion + 1]) {
        if (diferencia[posicion] < diferencia[posicion + 1]) {
          cambiar = true;
        }
      }

      if (cambiar) {
        let auxiliar = nombres[posicion];
        nombres[posicion] = nombres[posicion + 1];
        nombres[posicion + 1] = auxiliar;

        auxiliar = puntos[posicion];
        puntos[posicion] = puntos[posicion + 1];
        puntos[posicion + 1] = auxiliar;

        auxiliar = diferencia[posicion];
        diferencia[posicion] = diferencia[posicion + 1];
        diferencia[posicion + 1] = auxiliar;
      }
    }
  }
}

let nombres = ["Boca", "River", "Racing"];
let puntos = [12, 15, 12];
let diferencia = [8, 5, 10];

ordenar_tabla(nombres, puntos, diferencia);

console.log("Tabla de posiciones:");

for (let posicion = 0; posicion < nombres.length; posicion++) {
  console.log(
    "${posicion + 1}° ${nombres[posicion]} - ${puntos[posicion]} pts - DG ${diferencia[posicion]}",
  );
}
