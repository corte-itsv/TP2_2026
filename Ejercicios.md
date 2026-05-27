# Ejercicios

## 🟢 Nivel 1 — Funciones + Condicionales

---

### Ejercicio 01

**Temas:** Función · `if/elif/else` · `str`

Escribí una función llamada `clasificar_nota(nota)` que reciba una nota entera y devuelva su clasificación como string según esta tabla:

|Nota|Clasificación|
|---|---|
|10|`"Perfecto"`|
|8 o 9|`"Muy bueno"`|
|6 o 7|`"Aprobado"`|
|4 o 5|`"Desaprobado (cerca)"`|
|1, 2 o 3|`"Desaprobado (lejos)"`|
|Cualquier otro|`"Nota inválida"`|

Luego llamá a la función con las notas `10`, `7`, `4`, `0` y `11`, mostrando cada resultado.

**Salida esperada:**

```
10 → Perfecto
7 → Aprobado
4 → Desaprobado (cerca)
0 → Nota inválida
11 → Nota inválida
```

---

### Ejercicio 02

**Temas:** Función · `list` · `for` · `return`

Escribí una función llamada `calcular_promedio(notas)` que reciba una lista de notas (números) y devuelva el promedio redondeado a 2 decimales.

Si la lista está vacía, la función debe devolver `0`.

Luego probá la función con estas listas:

```python
lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []
```

**Salida esperada:**

```
Promedio A: 8.0
Promedio B: 4.5
Promedio C: 0
```

> 💡 **Pista:** Podés usar `sum()` y `len()`, o un bucle `for` acumulador.

---

### Ejercicio 03

**Temas:** Función · `list` · `for` · `if` · `return`

Escribí dos funciones:
min_max(numeros)
1. `contar_aprobados(notas)` → recibe una lista de notas y devuelve cuántas son **mayores o iguales a 6**.
2. `contar_desaprobados(notas)` → recibe una lista de notas y devuelve cuántas son **menores a 6**.

Probá ambas con esta lista ya definida en el código:

```python
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
```

**Salida esperada:**

```
Total: 10 alumnos
Aprobados: 6
Desaprobados: 4
```

---

### Ejercicio 04

**Temas:** Función · `list` · `for` · `if` · `tuple` · `return`

Escribí una función llamada `` que reciba una lista de números y devuelva una **tupla** con el valor mínimo y el valor máximo, **sin usar las funciones `min()` ni `max()`**.

La función debe recorrer la lista con un `for` y comparar valores.

Probá la función con esta lista:

```python
numeros = [34, 7, 89, 12, 56, 3, 78, 45]
```

Luego desempaquetá el resultado en dos variables.

**Salida esperada:**

```
Mínimo: 3
Máximo: 89
```

---

### Ejercicio 05

**Temas:** Función · `list` · `for` · `if` · `return`

Escribí una función llamada `filtrar_pares(numeros)` que reciba una lista de enteros y devuelva una **nueva lista** con solo los números pares.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

**Salida esperada:**

```
[2, 4, 6, 8, 10, 12]
```

---

## 🟡 Nivel 2 — Funciones + Listas y Tuplas

---

### Ejercicio 06

**Temas:** Función · `list` · `for` · `return`

Escribí una función llamada `invertir(lista)` que reciba una lista y devuelva una **nueva lista** con los elementos en orden inverso, **sin usar `.reverse()` ni slicing `[::-1]`**.

La función debe construir la nueva lista recorriéndola con un `for` o usando índices.

Probá con:

```python
original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]
```

**Salida esperada:**

```
[5, 4, 3, 2, 1]
['d', 'c', 'b', 'a']
```

---

### Ejercicio 07

**Temas:** Función · `list` · `for` · `if` · `break` · `return` · `bool`

Escribí dos funciones:

1. `esta_en_lista(lista, elemento)` → devuelve `True` si el elemento está en la lista, `False` si no. **No uses el operador `in`**.
2. `posicion_en_lista(lista, elemento)` → devuelve el **índice** de la primera aparición del elemento, o `-1` si no se encuentra.

Probá con esta lista:

```python
frutas = ["manzana", "banana", "pera", "uva", "kiwi"]
```

**Salida esperada:**

```
¿'pera' está en la lista? True
¿'mango' está en la lista? False
Posición de 'uva': 3
Posición de 'mango': -1
```

---

### Ejercicio 08

**Temas:** Función · `dict` · `for` · `if` · `str` · `return`

Escribí una función llamada `contar_frecuencia(palabras)` que reciba una lista de strings y devuelva un **diccionario** donde las claves son las palabras y los valores son la cantidad de veces que aparece cada una.

Luego escribí una función `palabra_mas_repetida(frecuencias)` que reciba ese diccionario y devuelva la palabra con mayor frecuencia.

Probá con:

```python
palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
```

**Salida esperada:**

```
{'python': 3, 'es': 2, 'genial': 1, 'facil': 1}
La palabra más repetida es: 'python' (3 veces)
```

---

### Ejercicio 09

**Temas:** Función · `dict` · `while` · `if/elif/else` · `break`

Implementá un sistema de agenda usando un diccionario. El diccionario guarda pares `nombre: teléfono`.

Escribí estas funciones:

- `agregar_contacto(agenda, nombre, telefono)` → agrega el par al diccionario.
- `buscar_contacto(agenda, nombre)` → devuelve el teléfono si existe, o `"Contacto no encontrado"` si no.
- `eliminar_contacto(agenda, nombre)` → elimina el contacto si existe.
- `mostrar_agenda(agenda)` → muestra todos los contactos ordenados por nombre.

Luego usá las funciones con estos datos ya definidos en el código:

```python
agenda = {}
agregar_contacto(agenda, "Ana",    "351-1234")
agregar_contacto(agenda, "Luis",   "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")
```

Y ejecutá estas operaciones en orden:

1. Mostrar la agenda completa.
2. Buscar a `"Luis"`.
3. Buscar a `"Pedro"`.
4. Eliminar a `"Marcos"`.
5. Mostrar la agenda final.

**Salida esperada:**

```
=== AGENDA ===
Ana: 351-1234
Luis: 351-5678
Marcos: 351-9012

Teléfono de Luis: 351-5678
Pedro: Contacto no encontrado

=== AGENDA ===
Ana: 351-1234
Luis: 351-5678
```

---

### Ejercicio 10

**Temas:** Función · `for` · `range()` · `list` · `return`

Escribí una función llamada `tabla_multiplicar(numero)` que reciba un número entero y devuelva una **lista de tuplas** con los pares `(multiplicador, resultado)` del 1 al 10.

Luego escribí una función `mostrar_tabla(tabla, numero)` que reciba esa lista y la muestre formateada.

Probá con `numero = 7`.

**Salida esperada:**

```
=== Tabla del 7 ===
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
```

---

## 🟠 Nivel 3 — Funciones + Sets y Diccionarios

---

### Ejercicio 11

**Temas:** Función · `list` · `set` · `return`

Escribí una función llamada `sin_duplicados(lista)` que reciba una lista con posibles elementos repetidos y devuelva una **nueva lista sin duplicados**, manteniendo el orden de primera aparición.

**No uses directamente `list(set(lista))`** porque los sets no preservan el orden. Implementalo con un `for` y un `set` auxiliar para rastrear los ya vistos.

Probá con:

```python
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]
```

**Salida esperada:**

```
[3, 1, 4, 5, 9, 2, 6]
['Ana', 'Luis', 'Sol', 'Marcos']
```

---

### Ejercicio 12

**Temas:** Función · `list` · `set` · operaciones de conjuntos · `return`

Escribí estas tres funciones usando operaciones de sets:

1. `interseccion(lista_a, lista_b)` → devuelve una lista con los elementos **presentes en ambas**.
2. `union(lista_a, lista_b)` → devuelve una lista con **todos los elementos sin repetir**.
3. `solo_en_a(lista_a, lista_b)` → devuelve una lista con los elementos de A que **no están en B**.

Probá con:

```python
clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]
```

**Salida esperada:**

```
Asistieron ambos días: ['Ana', 'Sol', 'Julia']
Asistieron al menos un día: ['Ana', 'Julia', 'Luis', 'Marcos', 'Pedro', 'Sol', 'Tomás']
Solo el lunes: ['Luis', 'Marcos']
```

> 💡 **Pista:** Convertí las listas a sets, operá con `&`, `|`, `-` y volvé a lista con `sorted()`.

---

### Ejercicio 13

**Temas:** Función · `dict` · `list` · `for` · `if` · `return`

Dado el siguiente diccionario ya definido en el código:

```python
curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}
```

Escribí estas funciones:

1. `calcular_promedios(curso)` → devuelve un nuevo diccionario `{nombre: promedio}` usando dict comprehension.
2. `alumno_destacado(promedios)` → devuelve el nombre del alumno con el mayor promedio.
3. `alumnos_aprobados(promedios)` → devuelve una lista con los nombres de quienes tienen promedio >= 6.

**Salida esperada:**

```
Promedios: {'Ana': 9.0, 'Luis': 6.0, 'Sol': 9.25, 'Marcos': 4.5, 'Julia': 7.75}
Alumno destacado: Sol (9.25)
Aprobados: ['Ana', 'Luis', 'Sol', 'Julia']
```

---

### Ejercicio 14

**Temas:** Función · `list` · List comprehension · `str` · `for` · `return`

Escribí estas cuatro funciones, cada una usando una **list comprehension**:

1. `a_mayusculas(palabras)` → devuelve la lista con todas las palabras en mayúsculas.
2. `longitudes(palabras)` → devuelve una lista con la longitud de cada palabra.
3. `filtrar_largas(palabras, minimo)` → devuelve solo las palabras con longitud mayor o igual a `minimo`.
4. `iniciales(palabras)` → devuelve una lista con la primera letra de cada palabra en mayúscula.

Probá con:

```python
palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]
```

**Salida esperada:**

```
Mayúsculas: ['PYTHON', 'PROGRAMACION', 'DATO', 'LISTA', 'FUNCION', 'SET', 'BUCLE']
Longitudes: [6, 12, 4, 5, 7, 3, 5]
Largas (>=6): ['python', 'programacion', 'funcion']
Iniciales: ['P', 'P', 'D', 'L', 'F', 'S', 'B']
```

---

### Ejercicio 15

**Temas:** Función · `dict` · `list` · `for` · `str` · `return`

Escribí una función llamada `agrupar_por_inicial(nombres)` que reciba una lista de nombres y devuelva un **diccionario** donde las claves son las letras iniciales y los valores son listas con los nombres que comienzan con esa letra.

Probá con:

```python
nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]
```

**Salida esperada:**

```
A: ['Ana', 'Alberto', 'Ana Paula']
B: ['Belen', 'Bruno']
C: ['Carlos', 'Camila']
D: ['Diego', 'Daniela']
```

> 💡 **Pista:** Usá `.get()` del diccionario para verificar si la clave ya existe, o inicializá con una lista vacía.

---

## 🔴 Nivel 4 — Ejercicios integradores

---

### Ejercicio 16

**Temas:** Función · `dict` · `list` · `for` · `if/elif` · `return` · f-strings

Dado el siguiente diccionario ya definido:

```python
curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}
```

Escribí las siguientes funciones y mostrá un **reporte completo** del curso:

1. `promedio(notas)` → promedio redondeado a 2 decimales.
2. `condicion(promedio)` → `"Aprobado"` si >= 6, `"Desaprobado"` si no.
3. `reporte_curso(curso)` → muestra una tabla con nombre, promedio y condición para cada alumno, ordenada de mayor a menor promedio.
4. `resumen(curso)` → muestra el promedio general del curso, el alumno con mejor promedio y el alumno con peor promedio.

**Salida esperada:**

```
======================================
          REPORTE DEL CURSO
======================================
Alumno     | Promedio | Condición
--------------------------------------
Sol        |     9.20 | Aprobado
Ana        |     8.60 | Aprobado
Julia      |     7.80 | Aprobado
Luis       |     5.60 | Desaprobado
Pedro      |     4.60 | Desaprobado
Marcos     |     4.00 | Desaprobado
======================================
Promedio general del curso: 6.63
Mejor promedio: Sol (9.20)
Peor promedio: Marcos (4.00)
```

---

### Ejercicio 17

**Temas:** Función · `str` · `for` · `ord()` · `chr()` · `return`

El **cifrado César** es un método de encriptación que desplaza cada letra del alfabeto un número fijo de posiciones.

Escribí dos funciones:

1. `cifrar(texto, desplazamiento)` → recibe un texto en minúsculas y un número de desplazamiento, y devuelve el texto cifrado. Los espacios y caracteres no alfabéticos se conservan sin cambio.
2. `descifrar(texto_cifrado, desplazamiento)` → devuelve el texto original.

> 💡 **Pistas:**
> 
> - `ord('a')` devuelve el código ASCII de `'a'` (97).
> - `chr(97)` devuelve el carácter con código ASCII 97 (`'a'`).
> - Para rotar dentro del alfabeto: `chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))`.

Probá con:

```python
mensaje = "hola mundo"
clave   = 3
```

**Salida esperada:**

```
Original:  hola mundo
Cifrado:   krod pxqgr
Descifrado: hola mundo
```

---

### Ejercicio 18

**Temas:** Función · `dict` · `list` · `for` · `if/elif/else` · `while` · `break`

Implementá un sistema de inventario usando un diccionario donde las claves son los nombres de los productos y los valores son diccionarios con `precio` y `stock`.

```python
inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}
```

Escribí estas funciones:

1. `agregar_producto(inv, nombre, precio, stock)` → agrega un nuevo producto.
2. `actualizar_stock(inv, nombre, cantidad)` → suma o resta cantidad al stock del producto. Si el stock queda negativo, no lo modifica y muestra `"Stock insuficiente"`.
3. `productos_sin_stock(inv)` → devuelve una lista con los nombres de productos con stock en 0.
4. `valor_total_inventario(inv)` → devuelve la suma de `precio * stock` de todos los productos.
5. `mostrar_inventario(inv)` → muestra todos los productos ordenados por nombre.

Ejecutá estas operaciones en orden y mostrá el estado final:

```python
agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)   # Stock insuficiente
actualizar_stock(inventario, "pera", -20)     # Queda en 0
```

**Salida esperada:**

```
Stock insuficiente para banana.

=== INVENTARIO ===
banana: $300 | Stock: 30
manzana: $500 | Stock: 50
pera: $700 | Stock: 0
uva: $900 | Stock: 15

Sin stock: ['pera']
Valor total: $43500
```

---

### Ejercicio 19

**Temas:** Función · `str` · `dict` · `list` · `set` · `for` · `return`

Dado el siguiente texto ya definido en el código:

```python
texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""
```

Escribí estas funciones:

1. `contar_palabras(texto)` → devuelve el total de palabras.
2. `palabras_unicas(texto)` → devuelve un `set` con las palabras sin repetir.
3. `frecuencia(texto)` → devuelve un diccionario `{palabra: cantidad}` ordenado de mayor a menor frecuencia.
4. `palabra_mas_comun(texto)` → devuelve la palabra que más se repite y cuántas veces.
5. `palabras_largas(texto, minimo)` → devuelve una lista de palabras con longitud >= `minimo`, sin repetir, ordenadas alfabéticamente.

> 💡 **Pista:** Usá `texto.lower().split()` para obtener la lista de palabras.

**Salida esperada:**

```
Total de palabras: 24
Palabras únicas: 17
Frecuencias:
  python       : 3
  es           : 3
  de           : 3
  y            : 2
  un           : 1
  ...
Palabra más común: 'python' (3 veces)
Palabras largas (>=7): ['aprender', 'artificial', 'ciencia', 'desarrollo', 'inteligencia', 'programacion']
```

---

### Ejercicio 20

**Temas:** Función · `dict` · `list` · `set` · `for` · `while` · `if/elif/else` · `break` · `return`

Implementá un sistema de votación escolar para elegir el delegado del curso.

El sistema tiene estas reglas:

- Solo pueden votar alumnos registrados (usar un `set`).
- Cada alumno solo puede votar una vez.
- Los candidatos son: `"Ana"`, `"Luis"`, `"Sol"`.
- Si el voto no es por un candidato válido, se cuenta como **voto en blanco**.

Escribí estas funciones:

1. `registrar_alumno(padron, nombre)` → agrega el nombre al set de alumnos habilitados.
2. `votar(votos, ya_votaron, nombre_votante, candidato, padron)` → registra el voto si el alumno está en el padrón y no votó antes. Si ya votó, muestra `"Ya votaste"`. Si no está en el padrón, muestra `"No estás habilitado para votar"`.
3. `resultado(votos)` → devuelve el diccionario de votos ordenado de mayor a menor.
4. `ganador(votos)` → devuelve el candidato con más votos.

Simulá la votación con estos datos ya definidos y mostrá los resultados:

```python
padron   = set()
ya_votaron = set()
votos    = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}

registrar_alumno(padron, "Valentina")
registrar_alumno(padron, "Tomás")
registrar_alumno(padron, "Camila")
registrar_alumno(padron, "Diego")
registrar_alumno(padron, "Lucía")

votar(votos, ya_votaron, "Valentina", "Ana",  padron)
votar(votos, ya_votaron, "Tomás",     "Sol",  padron)
votar(votos, ya_votaron, "Camila",    "Ana",  padron)
votar(votos, ya_votaron, "Diego",     "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol",  padron)  # ya votó
votar(votos, ya_votaron, "Pedro",     "Ana",  padron)  # no habilitado
votar(votos, ya_votaron, "Lucía",     "Marta",padron)  # candidato inválido → blanco
```

**Salida esperada:**

```
Valentina ya votó.
Pedro no está habilitado para votar.
Lucía votó en blanco.

=== RESULTADOS ===
Ana    : 2 votos
Sol    : 1 voto
Luis   : 1 voto
Blanco : 1 voto

🏆 Ganador/a: Ana con 2 votos
```
