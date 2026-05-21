import pytest

try:
    from ejercicio_06 import invertir
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_06.py no existe",
        allow_module_level=True,
    )

@pytest.mark.parametrize(
    "lista,esperado",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (["a", "b", "c", "d"], ["d", "c", "b", "a"]),
        ([1], [1]),
        ([], []),
        ([True, False, True], [True, False, True]),
    ],
)
def test_invertir(lista, esperado):
    assert invertir(lista) == esperado
