from __future__ import annotations

import argparse
import ast
import builtins
import contextlib
import io
import json
import math
import os
import re
import runpy
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
EXERCISES = tuple(range(1, 21))
SCRIPT_TIMEOUT_SECONDS = 5
EXERCISE_TIMEOUT_SECONDS = 12


@dataclass
class ExerciseResult:
    number: int
    path: str
    passed: bool
    failures: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(
            {
                "number": self.number,
                "path": self.path,
                "passed": self.passed,
                "failures": self.failures,
            },
            ensure_ascii=False,
        )


class ExerciseContext:
    def __init__(
        self,
        number: int,
        path: Path,
        namespace: dict[str, Any],
        tree: ast.AST,
        failures: list[str],
    ) -> None:
        self.number = number
        self.path = path
        self.namespace = namespace
        self.tree = tree
        self.failures = failures

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def require_callable(self, name: str) -> Callable[..., Any] | None:
        value = self.namespace.get(name)
        if not callable(value):
            self.fail(f"Falta definir la funcion {name}().")
            return None
        return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Corrector automatico del TP.")
    parser.add_argument("--exercise", type=int, choices=EXERCISES)
    args = parser.parse_args()

    if args.exercise is not None:
        result = run_one_exercise(args.exercise)
        print(result.to_json())
        return 0 if result.passed else 1

    return run_all_exercises()


def run_all_exercises() -> int:
    results: list[ExerciseResult] = []

    for number in EXERCISES:
        result = run_exercise_in_child(number)
        results.append(result)

    print("\nCorreccion de ejercicios")
    print("========================")
    for result in results:
        status = "OK" if result.passed else "FALLA"
        print(f"{status:5} ejercicio_{result.number:02d}.py")
        for failure in result.failures:
            print(f"      - {failure}")
            print_github_error(result.path, result.number, failure)

    passed = sum(1 for result in results if result.passed)
    total = len(results)
    print(f"\nResultado: {passed}/{total} ejercicios aprobados.")
    write_github_summary(results)
    return 0 if passed == total else 1


def run_exercise_in_child(number: int) -> ExerciseResult:
    command = [sys.executable, str(Path(__file__).resolve()), "--exercise", str(number)]
    path = f"ejercicio_{number:02d}.py"
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=EXERCISE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return ExerciseResult(
            number=number,
            path=path,
            passed=False,
            failures=[
                f"El corrector excedio {EXERCISE_TIMEOUT_SECONDS}s. "
                "Revisa loops infinitos o input() bloqueante."
            ],
        )

    stdout = completed.stdout.strip()
    try:
        payload = json.loads(stdout.splitlines()[-1])
    except (IndexError, json.JSONDecodeError):
        details = (completed.stderr or completed.stdout or "sin salida").strip()
        return ExerciseResult(
            number=number,
            path=path,
            passed=False,
            failures=[f"El corrector no pudo interpretar el resultado: {short(details)}"],
        )

    return ExerciseResult(
        number=payload["number"],
        path=payload["path"],
        passed=payload["passed"],
        failures=payload["failures"],
    )


def run_one_exercise(number: int) -> ExerciseResult:
    rel_path = f"ejercicio_{number:02d}.py"
    path = ROOT / rel_path
    failures: list[str] = []

    if not path.exists():
        return ExerciseResult(
            number=number,
            path=rel_path,
            passed=False,
            failures=[f"No existe el archivo {rel_path}."],
        )

    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ExerciseResult(
            number=number,
            path=rel_path,
            passed=False,
            failures=["El archivo no se puede leer como UTF-8."],
        )

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        message = f"Error de sintaxis en linea {exc.lineno}: {exc.msg}."
        return ExerciseResult(number, rel_path, False, [message])

    check_script_executes(path, failures)
    namespace = load_namespace(path, number, failures)
    if namespace is not None:
        context = ExerciseContext(number, path, namespace, tree, failures)
        TESTS[number](context)

    return ExerciseResult(number, rel_path, not failures, failures)


def check_script_executes(path: Path, failures: list[str]) -> None:
    try:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            input="",
            check=False,
            capture_output=True,
            text=True,
            timeout=SCRIPT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        failures.append(
            f"El archivo no termina en {SCRIPT_TIMEOUT_SECONDS}s al ejecutarse."
        )
        return

    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip()
        failures.append(f"El archivo falla al ejecutarse: {short(details)}")


def load_namespace(
    path: Path, number: int, failures: list[str]
) -> dict[str, Any] | None:
    original_input = builtins.input
    original_argv = sys.argv[:]

    def blocked_input(*_args: Any, **_kwargs: Any) -> str:
        raise RuntimeError("No se debe usar input(); los datos del TP ya estan definidos.")

    builtins.input = blocked_input
    sys.argv = [str(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ):
            return runpy.run_path(
                str(path), run_name=f"__corrector_ejercicio_{number:02d}__"
            )
    except SystemExit as exc:
        failures.append(f"El archivo llama a exit()/sys.exit() al importarse: {exc}.")
    except Exception as exc:  # noqa: BLE001 - el corrector debe reportar cualquier error.
        failures.append(f"El archivo falla al importarse: {type(exc).__name__}: {exc}")
    finally:
        builtins.input = original_input
        sys.argv = original_argv

    return None


def call_function(
    context: ExerciseContext,
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> tuple[bool, Any, str]:
    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(
            io.StringIO()
        ):
            value = func(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001 - se reporta como falla del ejercicio.
        context.fail(f"{func.__name__}() lanzo {type(exc).__name__}: {exc}")
        return False, None, stdout.getvalue()
    return True, value, stdout.getvalue()


def assert_equal(
    context: ExerciseContext, label: str, actual: Any, expected: Any
) -> None:
    if actual != expected:
        context.fail(f"{label}: se esperaba {expected!r}, se obtuvo {actual!r}.")


def assert_almost_equal(
    context: ExerciseContext, label: str, actual: Any, expected: float, ndigits: int = 2
) -> None:
    tolerance = 10 ** (-(ndigits + 2))
    if not isinstance(actual, (int, float)) or not math.isclose(
        float(actual), expected, abs_tol=tolerance
    ):
        context.fail(f"{label}: se esperaba {expected!r}, se obtuvo {actual!r}.")


def assert_mapping_almost_equal(
    context: ExerciseContext,
    label: str,
    actual: Any,
    expected: dict[Any, float],
) -> None:
    if not isinstance(actual, dict):
        context.fail(f"{label}: se esperaba un diccionario, se obtuvo {type(actual).__name__}.")
        return
    if set(actual) != set(expected):
        context.fail(f"{label}: claves esperadas {set(expected)!r}, obtenidas {set(actual)!r}.")
        return
    for key, expected_value in expected.items():
        assert_almost_equal(context, f"{label}[{key!r}]", actual[key], expected_value)


def compact_lines(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", line.strip()) for line in text.splitlines() if line.strip()]


def text_from_call(value: Any, stdout: str) -> str:
    if stdout.strip():
        return stdout
    if isinstance(value, str):
        return value
    return ""


def short(text: str, limit: int = 500) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def has_call_named(tree: ast.AST, names: set[str]) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in names:
                return True
    return False


def has_attribute_call(tree: ast.AST, attrs: set[str]) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in attrs:
                return True
    return False


def function_nodes(tree: ast.AST, name: str) -> list[ast.FunctionDef | ast.AsyncFunctionDef]:
    return [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name
    ]


def function_contains(tree: ast.AST, name: str, node_type: type[ast.AST]) -> bool:
    return any(
        isinstance(child, node_type)
        for node in function_nodes(tree, name)
        for child in ast.walk(node)
    )


def is_minus_one(node: ast.AST | None) -> bool:
    if node is None:
        return False
    if isinstance(node, ast.Constant) and node.value == -1:
        return True
    return (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.USub)
        and isinstance(node.operand, ast.Constant)
        and node.operand.value == 1
    )


def has_reverse_slice(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
            if is_minus_one(node.slice.step):
                return True
    return False


def has_in_operator(tree: ast.AST) -> bool:
    return any(
        isinstance(node, ast.Compare)
        and any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops)
        for node in ast.walk(tree)
    )


def has_direct_list_set(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "list":
            continue
        if not node.args:
            continue
        first_arg = node.args[0]
        if isinstance(first_arg, ast.Call) and isinstance(first_arg.func, ast.Name):
            if first_arg.func.id == "set":
                return True
    return False


def assert_sequence_has_exact_values(
    context: ExerciseContext, label: str, actual: Any, expected: list[Any]
) -> None:
    if not isinstance(actual, list):
        context.fail(f"{label}: se esperaba una lista, se obtuvo {type(actual).__name__}.")
        return
    if actual != expected:
        context.fail(f"{label}: se esperaba {expected!r}, se obtuvo {actual!r}.")


def test_01(context: ExerciseContext) -> None:
    func = context.require_callable("clasificar_nota")
    if func is None:
        return
    cases = {
        10: "Perfecto",
        9: "Muy bueno",
        8: "Muy bueno",
        7: "Aprobado",
        6: "Aprobado",
        5: "Desaprobado (cerca)",
        4: "Desaprobado (cerca)",
        3: "Desaprobado (lejos)",
        2: "Desaprobado (lejos)",
        1: "Desaprobado (lejos)",
        0: "Nota inválida",
        11: "Nota inválida",
        -1: "Nota inválida",
    }
    for nota, expected in cases.items():
        ok, actual, _ = call_function(context, func, nota)
        if ok:
            assert_equal(context, f"clasificar_nota({nota})", actual, expected)


def test_02(context: ExerciseContext) -> None:
    func = context.require_callable("calcular_promedio")
    if func is None:
        return
    cases = [
        ([8, 9, 7, 10, 6], 8.0),
        ([4, 5, 3, 6, 4, 5], 4.5),
        ([], 0),
        ([1, 2, 2], 1.67),
    ]
    for notas, expected in cases:
        ok, actual, _ = call_function(context, func, notas)
        if ok:
            assert_almost_equal(context, f"calcular_promedio({notas!r})", actual, expected)


def test_03(context: ExerciseContext) -> None:
    aprobados = context.require_callable("contar_aprobados")
    desaprobados = context.require_callable("contar_desaprobados")
    if aprobados is None or desaprobados is None:
        return
    notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
    ok, actual, _ = call_function(context, aprobados, notas)
    if ok:
        assert_equal(context, "contar_aprobados(lista del enunciado)", actual, 6)
    ok, actual, _ = call_function(context, desaprobados, notas)
    if ok:
        assert_equal(context, "contar_desaprobados(lista del enunciado)", actual, 4)
    ok, actual, _ = call_function(context, aprobados, [])
    if ok:
        assert_equal(context, "contar_aprobados([])", actual, 0)
    ok, actual, _ = call_function(context, desaprobados, [5.9, 6, 10, 0])
    if ok:
        assert_equal(context, "contar_desaprobados([5.9, 6, 10, 0])", actual, 2)


def test_04(context: ExerciseContext) -> None:
    func = context.require_callable("min_max")
    if func is None:
        return
    if has_call_named(context.tree, {"min", "max"}):
        context.fail("min_max() no debe usar min() ni max().")
    cases = [
        ([34, 7, 89, 12, 56, 3, 78, 45], (3, 89)),
        ([-2, -5, 0, 10], (-5, 10)),
        ([4], (4, 4)),
    ]
    for numeros, expected in cases:
        ok, actual, _ = call_function(context, func, numeros)
        if ok:
            assert_equal(context, f"min_max({numeros!r})", actual, expected)


def test_05(context: ExerciseContext) -> None:
    main_func = context.require_callable("filtrar_pares")
    candidates = [
        "filtrar_pares_a",
        "filtrar_pares_b",
        "filtrar_pares_for",
        "filtrar_pares_con_for",
        "filtrar_pares_comprehension",
        "filtrar_pares_comprension",
    ]
    if main_func is None:
        return
    functions = [
        context.namespace[name]
        for name in candidates
        if callable(context.namespace.get(name))
    ]
    functions.insert(0, main_func)
    if not has_attribute_call(context.tree, {"append"}):
        context.fail("Debe existir una version con for y append().")
    for func in functions:
        ok, actual, _ = call_function(
            context, func, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )
        if ok:
            assert_equal(context, f"{func.__name__}(lista del enunciado)", actual, [2, 4, 6, 8, 10, 12])
        ok, actual, _ = call_function(context, func, [0, -2, -3, 7, 8])
        if ok:
            assert_equal(context, f"{func.__name__}([0, -2, -3, 7, 8])", actual, [0, -2, 8])


def test_06(context: ExerciseContext) -> None:
    func = context.require_callable("invertir")
    if func is None:
        return
    if has_attribute_call(context.tree, {"reverse"}) or has_call_named(context.tree, {"reversed"}):
        context.fail("invertir() no debe usar reverse() ni reversed().")
    if has_reverse_slice(context.tree):
        context.fail("invertir() no debe usar slicing con paso -1.")
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (["a", "b", "c", "d"], ["d", "c", "b", "a"]),
        ([], []),
        ([1], [1]),
    ]
    for lista, expected in cases:
        ok, actual, _ = call_function(context, func, lista)
        if ok:
            assert_equal(context, f"invertir({lista!r})", actual, expected)


def test_07(context: ExerciseContext) -> None:
    esta = context.require_callable("esta_en_lista")
    posicion = context.require_callable("posicion_en_lista")
    if esta is None or posicion is None:
        return
    if has_in_operator(context.tree):
        context.fail("No se debe usar el operador in/not in para resolver este ejercicio.")
    frutas = ["manzana", "banana", "pera", "uva", "kiwi"]
    cases_bool = [
        ((frutas, "pera"), True),
        ((frutas, "mango"), False),
        (([], "x"), False),
    ]
    for args, expected in cases_bool:
        ok, actual, _ = call_function(context, esta, *args)
        if ok:
            assert_equal(context, f"esta_en_lista{args!r}", actual, expected)
    cases_pos = [
        ((frutas, "uva"), 3),
        ((frutas, "mango"), -1),
        ((["a", "b", "a"], "a"), 0),
    ]
    for args, expected in cases_pos:
        ok, actual, _ = call_function(context, posicion, *args)
        if ok:
            assert_equal(context, f"posicion_en_lista{args!r}", actual, expected)


def test_08(context: ExerciseContext) -> None:
    contar = context.require_callable("contar_frecuencia")
    mas = context.require_callable("palabra_mas_repetida")
    if contar is None or mas is None:
        return
    palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
    ok, freqs, _ = call_function(context, contar, palabras)
    if ok:
        assert_equal(
            context,
            "contar_frecuencia(lista del enunciado)",
            freqs,
            {"python": 3, "es": 2, "genial": 1, "facil": 1},
        )
        ok, actual, _ = call_function(context, mas, freqs)
        if ok:
            assert_equal(context, "palabra_mas_repetida(frecuencias)", actual, "python")
    ok, actual, _ = call_function(context, contar, [])
    if ok:
        assert_equal(context, "contar_frecuencia([])", actual, {})


def test_09(context: ExerciseContext) -> None:
    agregar = context.require_callable("agregar_contacto")
    buscar = context.require_callable("buscar_contacto")
    eliminar = context.require_callable("eliminar_contacto")
    mostrar = context.require_callable("mostrar_agenda")
    if None in (agregar, buscar, eliminar, mostrar):
        return
    agenda: dict[str, str] = {}
    for nombre, telefono in [
        ("Ana", "351-1234"),
        ("Luis", "351-5678"),
        ("Marcos", "351-9012"),
    ]:
        call_function(context, agregar, agenda, nombre, telefono)
    assert_equal(
        context,
        "agregar_contacto() debe modificar la agenda",
        agenda,
        {"Ana": "351-1234", "Luis": "351-5678", "Marcos": "351-9012"},
    )
    ok, actual, _ = call_function(context, buscar, agenda, "Luis")
    if ok:
        assert_equal(context, "buscar_contacto(agenda, 'Luis')", actual, "351-5678")
    ok, actual, _ = call_function(context, buscar, agenda, "Pedro")
    if ok:
        assert_equal(context, "buscar_contacto(agenda, 'Pedro')", actual, "Contacto no encontrado")
    ok, _, stdout = call_function(context, mostrar, agenda)
    if ok:
        lines = compact_lines(stdout)
        expected_lines = ["Ana: 351-1234", "Luis: 351-5678", "Marcos: 351-9012"]
        positions = [lines.index(line) for line in expected_lines if line in lines]
        if len(positions) != 3 or positions != sorted(positions):
            context.fail("mostrar_agenda() debe mostrar los contactos ordenados por nombre.")
    call_function(context, eliminar, agenda, "Marcos")
    assert_equal(context, "eliminar_contacto() debe borrar Marcos", agenda, {"Ana": "351-1234", "Luis": "351-5678"})


def test_10(context: ExerciseContext) -> None:
    tabla = context.require_callable("tabla_multiplicar")
    mostrar = context.require_callable("mostrar_tabla")
    if tabla is None or mostrar is None:
        return
    expected = [(i, 7 * i) for i in range(1, 11)]
    ok, actual, _ = call_function(context, tabla, 7)
    if ok:
        assert_equal(context, "tabla_multiplicar(7)", actual, expected)
    ok, generated, _ = call_function(context, tabla, 3)
    if ok:
        assert_equal(context, "tabla_multiplicar(3)", generated, [(i, 3 * i) for i in range(1, 11)])
    ok, _, stdout = call_function(context, mostrar, expected, 7)
    if ok:
        lines = compact_lines(stdout)
        if not lines or "Tabla del 7" not in lines[0]:
            context.fail("mostrar_tabla() debe imprimir el encabezado de la tabla.")
        for i in range(1, 11):
            pattern = re.compile(rf"^7\s*x\s*{i}\s*=\s*{7 * i}$")
            if not any(pattern.match(line) for line in lines):
                context.fail(f"mostrar_tabla() no imprimio correctamente la fila {i}.")


def test_11(context: ExerciseContext) -> None:
    func = context.require_callable("sin_duplicados")
    if func is None:
        return
    if has_direct_list_set(context.tree):
        context.fail("No se debe resolver con list(set(lista)); debe conservar el orden.")
    cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [3, 1, 4, 5, 9, 2, 6]),
        (["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"], ["Ana", "Luis", "Sol", "Marcos"]),
        ([], []),
        ([1, 1, 1], [1]),
    ]
    for lista, expected in cases:
        ok, actual, _ = call_function(context, func, lista)
        if ok:
            assert_equal(context, f"sin_duplicados({lista!r})", actual, expected)


def test_12(context: ExerciseContext) -> None:
    inter = context.require_callable("interseccion")
    unir = context.require_callable("union")
    solo = context.require_callable("solo_en_a")
    if inter is None or unir is None or solo is None:
        return
    if not has_call_named(context.tree, {"set"}) and not any(
        isinstance(node, (ast.Set, ast.SetComp)) for node in ast.walk(context.tree)
    ):
        context.fail("Se espera usar sets para resolver las operaciones de conjuntos.")
    lunes = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
    miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]
    cases = [
        (inter, (lunes, miercoles), {"Ana", "Sol", "Julia"}),
        (unir, (lunes, miercoles), {"Ana", "Luis", "Sol", "Marcos", "Julia", "Pedro", "Tomás"}),
        (solo, (lunes, miercoles), {"Luis", "Marcos"}),
    ]
    for func, args, expected in cases:
        ok, actual, _ = call_function(context, func, *args)
        if ok:
            if not isinstance(actual, list):
                context.fail(f"{func.__name__}() debe devolver una lista.")
            elif set(actual) != expected or len(actual) != len(expected):
                context.fail(f"{func.__name__}() devolvio {actual!r}, elementos esperados {expected!r}.")


def test_13(context: ExerciseContext) -> None:
    calcular = context.require_callable("calcular_promedios")
    destacado = context.require_callable("alumno_destacado")
    aprobados = context.require_callable("alumnos_aprobados")
    if calcular is None or destacado is None or aprobados is None:
        return
    if not any(isinstance(node, ast.DictComp) for node in ast.walk(context.tree)):
        context.fail("calcular_promedios() debe usar dict comprehension.")
    curso = {
        "Ana": [9, 10, 8, 9],
        "Luis": [6, 5, 7, 6],
        "Sol": [10, 9, 10, 8],
        "Marcos": [4, 5, 3, 6],
        "Julia": [7, 8, 7, 9],
    }
    expected = {"Ana": 9.0, "Luis": 6.0, "Sol": 9.25, "Marcos": 4.5, "Julia": 7.75}
    ok, promedios, _ = call_function(context, calcular, curso)
    if ok:
        assert_mapping_almost_equal(context, "calcular_promedios(curso)", promedios, expected)
        ok, actual, _ = call_function(context, destacado, promedios)
        if ok:
            assert_equal(context, "alumno_destacado(promedios)", actual, "Sol")
        ok, actual, _ = call_function(context, aprobados, promedios)
        if ok:
            assert_equal(context, "alumnos_aprobados(promedios)", actual, ["Ana", "Luis", "Sol", "Julia"])


def test_14(context: ExerciseContext) -> None:
    names = ["a_mayusculas", "longitudes", "filtrar_largas", "iniciales"]
    funcs = {name: context.require_callable(name) for name in names}
    if any(value is None for value in funcs.values()):
        return
    for name in names:
        if not function_contains(context.tree, name, ast.ListComp):
            context.fail(f"{name}() debe usar una list comprehension.")
    palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]
    cases = [
        ("a_mayusculas", (palabras,), ["PYTHON", "PROGRAMACION", "DATO", "LISTA", "FUNCION", "SET", "BUCLE"]),
        ("longitudes", (palabras,), [6, 12, 4, 5, 7, 3, 5]),
        ("filtrar_largas", (palabras, 6), ["python", "programacion", "funcion"]),
        ("iniciales", (palabras,), ["P", "P", "D", "L", "F", "S", "B"]),
    ]
    for name, args, expected in cases:
        ok, actual, _ = call_function(context, funcs[name], *args)
        if ok:
            assert_equal(context, f"{name}()", actual, expected)


def test_15(context: ExerciseContext) -> None:
    func = context.require_callable("agrupar_por_inicial")
    if func is None:
        return
    nombres = [
        "Ana",
        "Alberto",
        "Belen",
        "Bruno",
        "Carlos",
        "Camila",
        "Ana Paula",
        "Diego",
        "Daniela",
    ]
    expected = {
        "A": ["Ana", "Alberto", "Ana Paula"],
        "B": ["Belen", "Bruno"],
        "C": ["Carlos", "Camila"],
        "D": ["Diego", "Daniela"],
    }
    ok, actual, _ = call_function(context, func, nombres)
    if ok:
        assert_equal(context, "agrupar_por_inicial(lista del enunciado)", actual, expected)


def test_16(context: ExerciseContext) -> None:
    promedio = context.require_callable("promedio")
    condicion = context.require_callable("condicion")
    reporte = context.require_callable("reporte_curso")
    resumen = context.require_callable("resumen")
    if promedio is None or condicion is None or reporte is None or resumen is None:
        return
    ok, actual, _ = call_function(context, promedio, [9, 10, 8, 9, 7])
    if ok:
        assert_almost_equal(context, "promedio([9, 10, 8, 9, 7])", actual, 8.6)
    ok, actual, _ = call_function(context, promedio, [1, 2, 2])
    if ok:
        assert_almost_equal(context, "promedio([1, 2, 2])", actual, 1.67)
    for value, expected in [(6, "Aprobado"), (5.99, "Desaprobado")]:
        ok, actual, _ = call_function(context, condicion, value)
        if ok:
            assert_equal(context, f"condicion({value})", actual, expected)
    curso = {
        "Ana": [9, 10, 8, 9, 7],
        "Luis": [6, 5, 7, 6, 4],
        "Sol": [10, 9, 10, 8, 9],
        "Marcos": [4, 5, 3, 6, 2],
        "Julia": [7, 8, 7, 9, 8],
        "Pedro": [5, 4, 6, 5, 3],
    }
    ok, value, stdout = call_function(context, reporte, curso)
    if ok:
        lines = compact_lines(text_from_call(value, stdout))
        expected_order = ["Sol", "Ana", "Julia", "Luis", "Pedro", "Marcos"]
        indexes: list[int] = []
        for name in expected_order:
            matches = [idx for idx, line in enumerate(lines) if line.startswith(name)]
            if not matches:
                context.fail(f"reporte_curso() no muestra la fila de {name}.")
            else:
                indexes.append(matches[0])
        if len(indexes) == len(expected_order) and indexes != sorted(indexes):
            context.fail("reporte_curso() debe ordenar de mayor a menor promedio.")
    ok, value, stdout = call_function(context, resumen, curso)
    if ok:
        text = text_from_call(value, stdout)
        compact = " ".join(compact_lines(text))
        for expected_text in ["6.63", "Sol", "9.20", "Marcos", "4.00"]:
            if expected_text not in compact:
                context.fail(f"resumen() debe incluir {expected_text!r}.")


def test_17(context: ExerciseContext) -> None:
    cifrar = context.require_callable("cifrar")
    descifrar = context.require_callable("descifrar")
    if cifrar is None or descifrar is None:
        return
    cases = [
        ("hola mundo", 3, "krod pxqgr"),
        ("xyz", 3, "abc"),
        ("abc xyz!", 2, "cde zab!"),
    ]
    for texto, desplazamiento, expected in cases:
        ok, actual, _ = call_function(context, cifrar, texto, desplazamiento)
        if ok:
            assert_equal(context, f"cifrar({texto!r}, {desplazamiento})", actual, expected)
    ok, actual, _ = call_function(context, descifrar, "krod pxqgr", 3)
    if ok:
        assert_equal(context, "descifrar('krod pxqgr', 3)", actual, "hola mundo")
    ok, actual, _ = call_function(context, descifrar, "abc", 3)
    if ok:
        assert_equal(context, "descifrar('abc', 3)", actual, "xyz")


def test_18(context: ExerciseContext) -> None:
    agregar = context.require_callable("agregar_producto")
    actualizar = context.require_callable("actualizar_stock")
    sin_stock = context.require_callable("productos_sin_stock")
    valor_total = context.require_callable("valor_total_inventario")
    mostrar = context.require_callable("mostrar_inventario")
    if None in (agregar, actualizar, sin_stock, valor_total, mostrar):
        return
    inventario = {
        "manzana": {"precio": 500, "stock": 50},
        "banana": {"precio": 300, "stock": 30},
        "pera": {"precio": 700, "stock": 20},
    }
    call_function(context, agregar, inventario, "uva", 900, 15)
    if "uva" not in inventario or inventario["uva"] != {"precio": 900, "stock": 15}:
        context.fail("agregar_producto() debe agregar uva con precio y stock.")
    ok, _, stdout = call_function(context, actualizar, inventario, "banana", -35)
    if ok:
        if inventario["banana"]["stock"] != 30:
            context.fail("actualizar_stock() no debe dejar stock negativo.")
        if "Stock insuficiente" not in stdout or "banana" not in stdout:
            context.fail("actualizar_stock() debe informar stock insuficiente para banana.")
    call_function(context, actualizar, inventario, "pera", -20)
    assert_equal(context, "stock de pera luego de restar 20", inventario["pera"]["stock"], 0)
    ok, actual, _ = call_function(context, sin_stock, inventario)
    if ok:
        assert_equal(context, "productos_sin_stock(inventario)", actual, ["pera"])
    ok, actual, _ = call_function(context, valor_total, inventario)
    if ok:
        assert_equal(context, "valor_total_inventario(inventario)", actual, 47500)
    ok, _, stdout = call_function(context, mostrar, inventario)
    if ok:
        lines = compact_lines(stdout)
        expected_order = ["banana:", "manzana:", "pera:", "uva:"]
        indexes = []
        for prefix in expected_order:
            matches = [idx for idx, line in enumerate(lines) if line.startswith(prefix)]
            if not matches:
                context.fail(f"mostrar_inventario() no muestra {prefix}")
            else:
                indexes.append(matches[0])
        if len(indexes) == len(expected_order) and indexes != sorted(indexes):
            context.fail("mostrar_inventario() debe ordenar productos por nombre.")


def test_19(context: ExerciseContext) -> None:
    contar = context.require_callable("contar_palabras")
    unicas = context.require_callable("palabras_unicas")
    frecuencia = context.require_callable("frecuencia")
    comun = context.require_callable("palabra_mas_comun")
    largas = context.require_callable("palabras_largas")
    if None in (contar, unicas, frecuencia, comun, largas):
        return
    texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""
    ok, actual, _ = call_function(context, contar, texto)
    if ok:
        assert_equal(context, "contar_palabras(texto)", actual, 25)
    ok, actual, _ = call_function(context, unicas, texto)
    if ok:
        if not isinstance(actual, set) or len(actual) != 18:
            context.fail("palabras_unicas(texto) debe devolver un set de 18 palabras.")
    ok, freqs, _ = call_function(context, frecuencia, texto)
    if ok:
        expected_counts = {"python": 3, "es": 3, "de": 3, "y": 2}
        for key, expected in expected_counts.items():
            if not isinstance(freqs, dict) or freqs.get(key) != expected:
                context.fail(f"frecuencia(texto)[{key!r}] debe ser {expected}.")
        if isinstance(freqs, dict):
            values = list(freqs.values())
            if values != sorted(values, reverse=True):
                context.fail("frecuencia(texto) debe estar ordenado de mayor a menor frecuencia.")
    ok, actual, _ = call_function(context, comun, texto)
    if ok:
        if not isinstance(actual, (tuple, list)) or len(actual) != 2:
            context.fail("palabra_mas_comun(texto) debe devolver palabra y cantidad.")
        else:
            assert_equal(context, "palabra_mas_comun(texto)", tuple(actual), ("python", 3))
    ok, actual, _ = call_function(context, largas, texto, 7)
    if ok:
        assert_equal(
            context,
            "palabras_largas(texto, 7)",
            actual,
            ["aprender", "artificial", "ciencia", "desarrollo", "inteligencia", "lenguaje", "programacion"],
        )


def test_20(context: ExerciseContext) -> None:
    registrar = context.require_callable("registrar_alumno")
    votar = context.require_callable("votar")
    resultado = context.require_callable("resultado")
    ganador = context.require_callable("ganador")
    if registrar is None or votar is None or resultado is None or ganador is None:
        return
    padron: set[str] = set()
    ya_votaron: set[str] = set()
    votos = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}
    for nombre in ["Valentina", "Tomás", "Camila", "Diego", "Lucía"]:
        call_function(context, registrar, padron, nombre)
    assert_equal(
        context,
        "registrar_alumno() debe agregar alumnos al padron",
        padron,
        {"Valentina", "Tomás", "Camila", "Diego", "Lucía"},
    )
    operaciones = [
        ("Valentina", "Ana"),
        ("Tomás", "Sol"),
        ("Camila", "Ana"),
        ("Diego", "Luis"),
    ]
    for votante, candidato in operaciones:
        call_function(context, votar, votos, ya_votaron, votante, candidato, padron)
    ok, _, stdout = call_function(context, votar, votos, ya_votaron, "Valentina", "Sol", padron)
    if ok and "Valentina" not in stdout:
        context.fail("votar() debe informar cuando Valentina ya voto.")
    ok, _, stdout = call_function(context, votar, votos, ya_votaron, "Pedro", "Ana", padron)
    if ok and "Pedro" not in stdout:
        context.fail("votar() debe informar cuando Pedro no esta habilitado.")
    ok, _, stdout = call_function(context, votar, votos, ya_votaron, "Lucía", "Marta", padron)
    if ok and "blanco" not in stdout.lower():
        context.fail("votar() debe informar que Lucia voto en blanco.")
    assert_equal(
        context,
        "votos finales",
        votos,
        {"Ana": 2, "Luis": 1, "Sol": 1, "Blanco": 1},
    )
    ok, actual, _ = call_function(context, resultado, votos)
    if ok:
        if not isinstance(actual, dict) or actual != {"Ana": 2, "Luis": 1, "Sol": 1, "Blanco": 1}:
            context.fail("resultado(votos) debe devolver el diccionario de votos finales.")
        elif list(actual.values()) != sorted(actual.values(), reverse=True):
            context.fail("resultado(votos) debe estar ordenado de mayor a menor cantidad de votos.")
    ok, actual, _ = call_function(context, ganador, votos)
    if ok:
        assert_equal(context, "ganador(votos)", actual, "Ana")


TESTS: dict[int, Callable[[ExerciseContext], None]] = {
    1: test_01,
    2: test_02,
    3: test_03,
    4: test_04,
    5: test_05,
    6: test_06,
    7: test_07,
    8: test_08,
    9: test_09,
    10: test_10,
    11: test_11,
    12: test_12,
    13: test_13,
    14: test_14,
    15: test_15,
    16: test_16,
    17: test_17,
    18: test_18,
    19: test_19,
    20: test_20,
}


def print_github_error(path: str, number: int, message: str) -> None:
    escaped = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error file={path},title=Ejercicio {number:02d}::{escaped}")


def write_github_summary(results: list[ExerciseResult]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    passed = sum(1 for result in results if result.passed)
    lines = [
        "## Correccion de ejercicios",
        "",
        f"Resultado: **{passed}/{len(results)}** ejercicios aprobados.",
        "",
        "| Ejercicio | Estado | Observaciones |",
        "| --- | --- | --- |",
    ]
    for result in results:
        status = "OK" if result.passed else "FALLA"
        failures = "<br>".join(result.failures) if result.failures else "-"
        lines.append(f"| ejercicio_{result.number:02d}.py | {status} | {failures} |")

    with Path(summary_path).open("a", encoding="utf-8") as summary:
        summary.write("\n".join(lines))
        summary.write("\n")


if __name__ == "__main__":
    raise SystemExit(main())
