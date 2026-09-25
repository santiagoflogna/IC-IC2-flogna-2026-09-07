# Parte A

## A1 — Verbo correcto

a) Ver la lista de libros: GET, porque se utiliza para consultar datos sin modificarlos.

b) Agregar un libro nuevo: POST, porque se utiliza para crear un recurso nuevo.

c) Borrar un libro: DELETE, porque se utiliza para eliminar un recurso existente.

d) Cambiarle el precio a un libro: PATCH, porque se modifica solamente una parte del recurso.

e) Reemplazar un libro entero por otro: PUT, porque reemplaza completamente el recurso existente.

f) Cambiarle solo la disponibilidad a un libro: PATCH, porque se modifica únicamente un campo sin tocar los demás.

La diferencia entre PUT y PATCH es que PUT reemplaza el recurso completo, mientras que PATCH modifica solamente una parte.

## A2 — Leer códigos de estado

200 — OK: indica que la petición salió correctamente.  
Ejemplo: hago `GET /libros` y la API devuelve la lista de libros.

201 — Created: indica que se creó un recurso correctamente.  
Ejemplo: hago `POST /libros` con un libro nuevo y la API lo agrega.

204 — No Content: indica que la operación salió correctamente, pero no hay contenido para devolver.  
Ejemplo: hago `DELETE /libros/1984`, el libro se elimina y la respuesta no devuelve un body.

400 — Bad Request: indica que el pedido está mal formado a nivel HTTP.  
Ejemplo: intento crear un libro enviando un body que no es un JSON válido.

404 — Not Found: indica que el recurso solicitado no existe.  
Ejemplo: hago `GET /libros/1984` y ese libro no está cargado.

405 — Method Not Allowed: indica que la URL existe, pero no acepta el verbo HTTP utilizado.  
Ejemplo: hago `DELETE /libros` cuando ese endpoint solamente acepta GET y POST.

422 — Unprocessable Entity: indica que la API entendió el pedido, pero los datos no cumplen con el contrato esperado.  
Ejemplo: hago `POST /libros` sin el campo `paginas`, o mando `"paginas": "muchas"` cuando la API espera un número.

500 — Internal Server Error: indica que ocurrió un error interno en el servidor.  
Ejemplo: el código de la API falla mientras intenta procesar un libro.

## A3 — Familias de códigos

2xx: indica que la petición salió correctamente.

3xx: indica una redirección, es decir, que lo pedido se encuentra en otro lugar o que hay que seguir otra dirección.

4xx: indica que hubo un problema con el pedido realizado por el cliente.

5xx: indica que ocurrió un problema interno en el servidor.

301 pertenece a la familia 3xx, por lo tanto corresponde a una redirección.

403 pertenece a la familia 4xx, por lo tanto indica un problema del lado del cliente.

## A4 — JSON a mano

Libro:

```json
{
  "titulo": "1984",
  "autor": "George Orwell",
  "paginas": 328,
  "disponible": true
}
```

Lista de 2 libros:

```json
[
  {
    "titulo": "1984",
    "autor": "George Orwell",
    "paginas": 328,
    "disponible": true
  },
  {
    "titulo": "El principito",
    "autor": "Antoine de Saint-Exupéry",
    "paginas": 96,
    "disponible": false
  }
]
```

Libro con editorial anidada:

```json
{
  "titulo": "1984",
  "autor": "George Orwell",
  "paginas": 328,
  "disponible": true,
  "editorial": {
    "nombre": "Debolsillo",
    "pais": "España"
  }
}
```


## A5 — Idempotencia

Un pedido es idempotente cuando hacerlo una vez o varias veces seguidas deja el mismo resultado final.

GET es idempotente porque consultar un recurso varias veces no modifica los datos.

POST normalmente no es idempotente porque cada vez que se envía puede crear un recurso nuevo.  

PUT es idempotente porque reemplaza un recurso por los mismos datos.  

DELETE es idempotente porque, una vez eliminado el recurso, repetir la operación no cambia el resultado final: el recurso sigue sin existir.


## A6 — Headers, lo mínimo

El header `Content-Type: application/json` le indica al servidor que el contenido enviado en el body está en formato JSON.

No forma parte de los datos del body, sino que es un metadato que le dice al servidor cómo interpretar esos datos.

Si un cliente manda un body JSON sin el header correcto, el servidor puede no interpretarlo como JSON y el pedido puede fallar, aunque el contenido esté bien escrito.

Por eso el header no es decorativo: sirve para indicar qué tipo de contenido se está enviando.


## A7 — Diseñar URLs (REST básico)

Listar todos los libros:

`GET /libros`

Se usa GET porque queremos consultar la lista completa de libros.

Ver un libro puntual:

`GET /libros/{id}`

Se usa GET porque queremos consultar un libro específico. El `{id}` identifica qué libro queremos ver.

Listar los libros de un autor puntual:

`GET /autores/{id}/libros`

Se usa GET porque queremos consultar los libros relacionados con un autor específico.

Crear un autor:

`POST /autores`

Se usa POST porque queremos crear un nuevo recurso dentro de autores.