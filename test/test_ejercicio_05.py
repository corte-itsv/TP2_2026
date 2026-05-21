import pytest

try:
    from ejercicio_05 import filtrar_pares
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_05.py no existe",
        allow_module_level=True,
    )


@pytest.mark.parametrize(
    "numeros,esperado",
    [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [2, 4, 6, 8, 10, 12],
        ),
        ([1, 3, 5], []),
        ([2, 4, 6], [2, 4, 6]),
        ([], []),
        ([0, 1, -2, -3, 8], [0, -2, 8]),
    ],
)
def test_filtrar_pares(numeros, esperado):
    assert filtrar_pares(numeros) == esperado
