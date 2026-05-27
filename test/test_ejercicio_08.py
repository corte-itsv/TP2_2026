import pytest

try:
    from ejercicio_08 import (
        contar_frecuencia,
        palabra_mas_repetida,
    )
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_08.py no existe",
        allow_module_level=True,
    )


@pytest.mark.parametrize(
    "palabras,esperado",
    [
        (
            ["python", "es", "genial", "python", "es", "facil", "python"],
            {
                "python": 3,
                "es": 2,
                "genial": 1,
                "facil": 1,
            },
        ),
        (
            ["a", "b", "a", "c", "b", "a"],
            {
                "a": 3,
                "b": 2,
                "c": 1,
            },
        ),
        (
            [],
            {},
        ),
        (
            ["hola"],
            {"hola": 1},
        ),
    ],
)
def test_contar_frecuencia(palabras, esperado):
    assert contar_frecuencia(palabras) == esperado


@pytest.mark.parametrize(
    "frecuencias,esperado",
    [
        (
            {
                "python": 3,
                "es": 2,
                "genial": 1,
                "facil": 1,
            },
            "python",
        ),
        (
            {
                "a": 5,
                "b": 2,
                "c": 1,
            },
            "a",
        ),
        (
            {"hola": 1},
            "hola",
        ),
    ],
)
def test_palabra_mas_repetida(frecuencias, esperado):
    assert palabra_mas_repetida(frecuencias) == esperado
