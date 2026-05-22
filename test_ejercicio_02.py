import pytest

try:
    from ejercicio_02 import (
            calcular_promedio
    )
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_02.py no existe",
        allow_module_level=True,
    )

@pytest.mark.parametrize(
    "notas,esperado",
    [
        ([8, 9, 7, 10, 6], 8.0),
        ([4, 5, 3, 6, 4, 5], 4.5),
        ([], 0),
        ([10], 10.0),
        ([1, 2, 3], 2.0),
        ([7.5, 8.5], 8.0),
        ([6, 7, 8], 7.0),
    ],
)
def test_calcular_promedio(notas, esperado):
    assert calcular_promedio(notas) == esperado