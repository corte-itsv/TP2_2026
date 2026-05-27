import pytest

try:
    from ejercicio_04 import min_max
except ModuleNotFoundError:
    pytest.skip(
        "ejercicio_04.py no existe",
        allow_module_level=True,
    )


@pytest.mark.parametrize(
    "numeros,esperado",
    [
        ([34, 7, 89, 12, 56, 3, 78, 45], (3, 89)),
        ([1, 2, 3, 4, 5], (1, 5)),
        ([5], (5, 5)),
        ([-10, 0, 10], (-10, 10)),
        ([7, 7, 7], (7, 7)),
        ([-5, -2, -20, -1], (-20, -1)),
    ],
)
def test_min_max(numeros, esperado):
    assert min_max(numeros) == esperado