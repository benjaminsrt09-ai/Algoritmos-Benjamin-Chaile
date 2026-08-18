/*Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.*/


function reservar_consecutivos(sala, fila, cantidad) {
  let total = sala[fila].length;

  for (let inicio = 0; inicio <= total - cantidad; inicio++) {
    let disponibles = true;

    for (let posicion = inicio; posicion < inicio + cantidad; posicion++) {
      if (sala[fila][posicion] === 1) {
        disponibles = false;
        break;
      }
    }

    if (disponibles) {
      let reservadas = [];

      for (let posicion = inicio; posicion < inicio + cantidad; posicion++) {
        sala[fila][posicion] = 1;
        reservadas.push(posicion);
      }

      return "Reserva confirmada. Columnas: " + reservadas.join(", ");
    }
  }

  return "No fue posible realizar la reserva.";
}

let matriz = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 1, 0, 0],
];

console.log(reservar_consecutivos(matriz, 2, 2));
console.log(matriz);

