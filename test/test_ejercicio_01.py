import pytest

try:
    from ejercicio_01 import (
            clasificar_nota
    )
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_01.py no existe",
        allow_module_level=True,
    )

@pytest.mark.parametrize(
    "nota,esperado",
    [
        (10, "Perfecto"),
        (8, "Muy bueno"),
        (9, "Muy bueno"),
        (6, "Aprobado"),
        (7, "Aprobado"),
        (4, "Desaprobado (cerca)"),
        (5, "Desaprobado (cerca)"),
        (1, "Desaprobado (lejos)"),
        (2, "Desaprobado (lejos)"),
        (3, "Desaprobado (lejos)"),
        (0, "Nota inválida"),
        (11, "Nota inválida"),
    ],
)
def test_clasificar_nota(nota, esperado):
    assert clasificar_nota(nota) == esperado
