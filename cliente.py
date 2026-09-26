import requests


url = "http://127.0.0.1:8000/libros"

sesion = requests.Session()


def mostrar_estado(respuesta):
    if (
        respuesta.status_code == 200
        or respuesta.status_code == 201
        or respuesta.status_code == 204
    ):
        print("ok")
    elif respuesta.status_code == 422:
        print("dato inválido")
    elif respuesta.status_code == 404:
        print("no existe")
    else:
        print("Código de estado:", respuesta.status_code)



def reemplazar_libro(titulo, libro_nuevo):
    respuesta = sesion.put(
        url + "/" + titulo,
        json=libro_nuevo
    )

    print("Respuesta del PUT:")
    mostrar_estado(respuesta)

    if respuesta.status_code != 204:
        print(respuesta.json())



def borrar_libro(titulo):
    respuesta = sesion.delete(
        url + "/" + titulo
    )

    print("Respuesta del DELETE:")
    mostrar_estado(respuesta)

    if respuesta.status_code != 204:
        print(respuesta.json())


try:


    respuesta = sesion.get(url)

    print("Libros antes del POST:")
    mostrar_estado(respuesta)
    print(respuesta.json())



    nuevo_libro = {
        "titulo": "Rayuela",
        "paginas": 600,
        "editorial": {
            "nombre": "Alfaguara",
            "pais": "España"
        },
        "disponible": True
    }

    respuesta_post = sesion.post(
        url,
        json=nuevo_libro
    )

    print("Respuesta del POST:")
    mostrar_estado(respuesta_post)
    print(respuesta_post.json())



    respuesta = sesion.get(url)

    print("Libros después del POST:")
    mostrar_estado(respuesta)
    print(respuesta.json())



    respuesta_no_existe = sesion.get(
        "http://127.0.0.1:8000/libros/Libro inexistente"
    )

    print("Prueba de libro inexistente:")
    mostrar_estado(respuesta_no_existe)
    print(respuesta_no_existe.json())



    libro_actualizado = {
        "titulo": "Rayuela actualizada",
        "paginas": 650,
        "editorial": {
            "nombre": "Alfaguara",
            "pais": "Argentina"
        },
        "disponible": False
    }

    reemplazar_libro("Rayuela", libro_actualizado)



    respuesta = sesion.get(url)

    print("Libros después del PUT:")
    mostrar_estado(respuesta)
    print(respuesta.json())



    borrar_libro("Rayuela actualizada")



    respuesta = sesion.get(url)

    print("Libros después del DELETE:")
    mostrar_estado(respuesta)
    print(respuesta.json())



    print("Prueba de timeout:")

    respuesta_timeout = sesion.get(
        "http://10.255.255.1/",
        timeout=1
    )

    print(respuesta_timeout.status_code)


except requests.exceptions.Timeout:
    print("La solicitud tardó demasiado tiempo")


except requests.exceptions.ConnectionError:
    print("No se pudo conectar con la API")