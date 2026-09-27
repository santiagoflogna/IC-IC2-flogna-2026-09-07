# Parte D - MQTT

## D1 - Ver el mensaje viajar

Se utilizó un cliente MQTT suscripto al topic:

`unraf/demo/saludo`

Desde otro cliente se publicó el mensaje:

`Hola MQTT FINAL`

El mensaje llegó correctamente al cliente suscripto.

En MQTT, el publicador envía el mensaje al broker y el broker lo entrega a los clientes que estén suscriptos al mismo topic.


## D2 - Publicar sin suscriptores

Primero se publicó un mensaje en el topic:

`unraf/demo/saludo`

sin que hubiera ningún cliente suscripto.

Luego se creó la suscripción al topic, pero el mensaje publicado anteriormente no apareció.

Después se publicó un nuevo mensaje con el cliente ya suscripto y este sí fue recibido.

Esto muestra que el publicador envía el mensaje sin saber si hay alguien escuchando y que, por defecto, un mensaje publicado antes de que exista un suscriptor se pierde.


## D3 - Pub/Sub vs Request/Response

En una API se utiliza el modelo request/response: un cliente realiza una petición y espera una respuesta del servidor. Por ejemplo, para consultar la información de un libro.

En MQTT se utiliza publish/subscribe: un cliente publica un mensaje en un topic y los clientes suscriptos pueden recibirlo sin que el publicador sepa quiénes son. Por ejemplo, para que un sensor publique continuamente mediciones de temperatura.


## D4 - Topics y jerarquía

Si los sensores publican en:

`casa/cocina/temp`

y

`casa/cocina/hum`

para recibir todo lo relacionado con la cocina se puede usar:

`casa/cocina/#`

En MQTT, `+` reemplaza un solo nivel del topic, mientras que `#` representa todos los niveles restantes.

Por ejemplo:

`casa/+/temp`

permite recibir la temperatura de distintos ambientes.

En cambio:

`casa/cocina/#`

permite recibir todos los mensajes que estén dentro de la jerarquía de la cocina.

## D5 - Diseño de topics

Se propone la siguiente estructura:

`casa/cocina/temperatura`
`casa/cocina/humedad`

`casa/living/temperatura`
`casa/living/humedad`

`casa/habitacion/temperatura`
`casa/habitacion/humedad`

La jerarquía utilizada es:

`casa/ambiente/tipo_de_sensor`

Esto permite usar wildcards para distintas suscripciones.

Para recibir todo:

`casa/#`

Para recibir todo lo de un ambiente:

`casa/cocina/#`

Para recibir un tipo de sensor de todos los ambientes:

`casa/+/temperatura`

De esta forma, la jerarquía permite organizar los mensajes y suscribirse de manera flexible.


## D6 - QoS

MQTT posee tres niveles de QoS:

- QoS 0: el mensaje se envía sin garantía de entrega.
- QoS 1: el mensaje llega al menos una vez, aunque puede llegar duplicado.
- QoS 2: el mensaje llega exactamente una vez.

Para un sensor de temperatura que publica cada 2 segundos utilizaría QoS 0, ya que si se pierde una lectura rápidamente llegará una nueva y se reduce el intercambio de mensajes.

Para un comando puntual como "abrir la puerta" utilizaría QoS 2, ya que es importante que el mensaje llegue y que no se procese más de una vez.


## D7 - Mensajes retenidos

Un mensaje retained es un mensaje que el broker conserva como último valor conocido de un topic.

Si un cliente se suscribe después de que el mensaje fue publicado, puede recibir inmediatamente ese último mensaje retenido.

La diferencia con D2 es que, sin retained, un cliente que se suscribe tarde no recibe los mensajes anteriores. Con retained, recibe el último mensaje guardado por el broker.

Esto es útil, por ejemplo, para conocer el último estado de un sensor sin tener que esperar a que publique nuevamente.



## D8 - MQTT vs polling

En polling, el cliente consulta periódicamente al servidor para saber si existe información nueva, aunque no haya ocurrido ningún cambio.

En MQTT, el cliente se suscribe a un topic y recibe los mensajes cuando son publicados, sin tener que consultar constantemente.

MQTT resulta conveniente para sistemas de sensores e IoT porque reduce consultas innecesarias y permite recibir los cambios cuando ocurren.