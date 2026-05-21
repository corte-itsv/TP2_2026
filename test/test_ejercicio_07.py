import pytest

try:
    from ejercicio_07 import (
        esta_en_lista,
        posicion_en_lista,
    )
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_07.py no existe",
        allow_module_level=True,
    )


@pytest.mark.parametrize(
    "lista,elemento,esperado",
    [
        (["manzana", "banana", "pera", "uva", "kiwi"], "pera", True),
        (["manzana", "banana", "pera", "uva", "kiwi"], "mango", False),
        ([1, 2, 3, 4], 3, True),
        ([1, 2, 3, 4], 10, False),
        ([], "algo", False),
    ],
)
def test_esta_en_lista(lista, elemento, esperado):
    assert esta_en_lista(lista, elemento) == esperado


@pytest.mark.parametrize(
    "lista,elemento,esperado",
    [
        (["manzana", "banana", "pera", "uva", "kiwi"], "uva", 3),
        (["manzana", "banana", "pera", "uva", "kiwi"], "mango", -1),
        ([1, 2, 3, 2, 1], 2, 1),
        ([1, 2, 3], 10, -1),
        ([], "algo", -1),
    ],
)
def test_posicion_en_lista(lista, elemento, esperado):
    assert posicion_en_lista(lista, elemento) == esperado
