/*Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato &quot;ID:TIPO:MONTO&quot;, donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
&quot;sospechosas&quot;. Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: &quot;TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000&quot; Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: [&#39;TX103&#39;]*/


function procesar_transacciones(texto) {
  let transacciones = texto.split(",");
  let saldo = 0;
  let sospechosas = [];

  for (let transaccion of transacciones) {
    let informacion = transaccion.trim().split(":");

    let id = informacion[0];
    let operacion = informacion[1];
    let dinero = parseInt(informacion[2]);

    if (operacion === "I") {
      saldo += dinero;
    } else if (operacion === "E") {
      saldo -= dinero;

      if (dinero > 50000) {
        sospechosas.push(id);
      }
    }
  }

  return [saldo, sospechosas];
}

let cadena = "TX101:I:120000, TX102:E:15000, TX103:E:85000, TX104:I:3000";

let resultado = procesar_transacciones(cadena);

let saldo = resultado[0];
let sospechosas = resultado[1];

console.log("Balance final: $" + saldo);
console.log("Transacciones sospechosas:", sospechosas);
