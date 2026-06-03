Ejercicio 17

Temas: Función · str · for · ord() · chr() · return

El cifrado César es un método de encriptación que desplaza cada letra del alfabeto un número fijo de posiciones.

Escribí dos funciones:

cifrar(texto, desplazamiento) → recibe un texto en minúsculas y un número de desplazamiento, y devuelve el texto cifrado. Los espacios y caracteres no alfabéticos se conservan sin cambio.
descifrar(texto_cifrado, desplazamiento) → devuelve el texto original.
💡 Pistas:

ord('a') devuelve el código ASCII de 'a' (97).
chr(97) devuelve el carácter con código ASCII 97 ('a').
Para rotar dentro del alfabeto: chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a')).
Probá con:

mensaje = "hola mundo"
clave   = 3
Salida esperada:

Original:  hola mundo
Cifrado:   krod pxqgr
Descifrado: hola mundo
Ejercicio 18

Temas: Función · dict · list · for · if/elif/else · while · break

Implementá un sistema de inventario usando un diccionario donde las claves son los nombres de los productos y los valores son diccionarios con precio y stock.

inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}
Escribí estas funciones:

agregar_producto(inv, nombre, precio, stock) → agrega un nuevo producto.
actualizar_stock(inv, nombre, cantidad) → suma o resta cantidad al stock del producto. Si el stock queda negativo, no lo modifica y muestra "Stock insuficiente".
productos_sin_stock(inv) → devuelve una lista con los nombres de productos con stock en 0.
valor_total_inventario(inv) → devuelve la suma de precio * stock de todos los productos.
mostrar_inventario(inv) → muestra todos los productos ordenados por nombre.
Ejecutá estas operaciones en orden y mostrá el estado final:

agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)   # Stock insuficiente
actualizar_stock(inventario, "pera", -20)     # Queda en 0
Salida esperada:

Stock insuficiente para banana.

=== INVENTARIO ===
banana: $300 | Stock: 30
manzana: $500 | Stock: 50
pera: $700 | Stock: 0
uva: $900 | Stock: 15

Sin stock: ['pera']
Valor total: $43500
Ejercicio 19

Temas: Función · str · dict · list · set · for · return

Dado el siguiente texto ya definido en el código:

texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""
Escribí estas funciones:

contar_palabras(texto) → devuelve el total de palabras.
palabras_unicas(texto) → devuelve un set con las palabras sin repetir.
frecuencia(texto) → devuelve un diccionario {palabra: cantidad} ordenado de mayor a menor frecuencia.
palabra_mas_comun(texto) → devuelve la palabra que más se repite y cuántas veces.
palabras_largas(texto, minimo) → devuelve una lista de palabras con longitud >= minimo, sin repetir, ordenadas alfabéticamente.
💡 Pista: Usá texto.lower().split() para obtener la lista de palabras.
Salida esperada:

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
Ejercicio 20

Temas: Función · dict · list · set · for · while · if/elif/else · break · return

Implementá un sistema de votación escolar para elegir el delegado del curso.

El sistema tiene estas reglas:

Solo pueden votar alumnos registrados (usar un set).
Cada alumno solo puede votar una vez.
Los candidatos son: "Ana", "Luis", "Sol".
Si el voto no es por un candidato válido, se cuenta como voto en blanco.
Escribí estas funciones:

registrar_alumno(padron, nombre) → agrega el nombre al set de alumnos habilitados.
votar(votos, ya_votaron, nombre_votante, candidato, padron) → registra el voto si el alumno está en el padrón y no votó antes. Si ya votó, muestra "Ya votaste". Si no está en el padrón, muestra "No estás habilitado para votar".
resultado(votos) → devuelve el diccionario de votos ordenado de mayor a menor.
ganador(votos) → devuelve el candidato con más votos.
Simulá la votación con estos datos ya definidos y mostrá los resultados:

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
Salida esperada:

Valentina ya votó.
Pedro no está habilitado para votar.
Lucía votó en blanco.

=== RESULTADOS ===
Ana    : 2 votos
Sol    : 1 voto
Luis   : 1 voto
Blanco : 1 voto

🏆 Ganador/a: Ana con 2 votos