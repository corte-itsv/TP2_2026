import pytest

try:
    from ejercicio_03 import (
        contar_aprobados,
        contar_desaprobados,
    )
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_03.py no existe",
        allow_module_level=True,
    )


@pytest.mark.parametrize(
    "notas,esperado",
    [
        ([8, 3, 6, 10, 4, 7, 5, 9, 6, 2], 6),
        ([6, 7, 8], 3),
        ([1, 2, 3], 0),
        ([], 0),
        ([5, 6, 5, 6], 2),
    ],
)
def test_contar_aprobados(notas, esperado):
    assert contar_aprobados(notas) == esperado


@pytest.mark.parametrize(
    "notas,esperado",
    [
        ([8, 3, 6, 10, 4, 7, 5, 9, 6, 2], 4),
        ([6, 7, 8], 0),
        ([1, 2, 3], 3),
        ([], 0),
        ([5, 6, 5, 6], 2),
    ],
)
def test_contar_desaprobados(notas, esperado):
    assert contar_desaprobados(notas) == esperado
