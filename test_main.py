from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_listar_libros():
    respuesta = client.get("/libros")

    assert respuesta.status_code == 200


def test_crear_libro_invalido():
    libro_invalido = {
        "titulo": "Libro de prueba",
        "paginas": 0,
        "editorial": {
            "nombre": "Editorial prueba",
            "pais": "Argentina"
        },
        "disponible": True
    }

    respuesta = client.post(
        "/libros",
        json=libro_invalido
    )

    assert respuesta.status_code == 422


def test_crear_libro_valido():
    libro_valido = {
        "titulo": "Dune",
        "paginas": 500,
        "editorial": {
            "nombre": "Debolsillo",
            "pais": "España"
        },
        "disponible": True
    }

    respuesta = client.post(
        "/libros",
        json=libro_valido
    )

    assert respuesta.status_code == 201


def test_post_y_get_libro():
    libro_nuevo = {
        "titulo": "Libro E4",
        "paginas": 300,
        "editorial": {
            "nombre": "Editorial E4",
            "pais": "Argentina"
        },
        "disponible": True
    }

    respuesta_post = client.post(
        "/libros",
        json=libro_nuevo
    )

    assert respuesta_post.status_code == 201

    respuesta_get = client.get("/libros")

    assert respuesta_get.status_code == 200

    libros = respuesta_get.json()

    encontrado = False

    for libro in libros:
        if libro["titulo"] == "Libro E4":
            encontrado = True

    assert encontrado == True