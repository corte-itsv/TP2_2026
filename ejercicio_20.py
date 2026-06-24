"""
Programación I - Evaluación Práctica

Gestor de Figuritas del Mundial

# TOTAL DE 55 puntos

El programa permitirá registrar las figuritas obtenidas para distintas
secciónes del álbum del Mundial.

Cada sección posee figuritas numeradas del 1 al 39.

Complete el código solicitado en cada función.
NO modifique los prototipos de las funciones ni las variables globales.

Es válido declarar funciones extra de ser considerarlo conveniente.

No está permitido declarar otras variables globales.
"""

# -----------------------------
# Datos provistos
# -----------------------------

ALBUM_COMPLETO = {
    "ARG": range(1, 40),
    "BRA": range(1, 40),
    "URU": range(1, 40),
    "ALE": range(1, 40),
    "ESP": range(1, 40),
    "FRA": range(1, 40)
}

# Conjunto con todas las secciones válidas.
SECCIONES = set(ALBUM_COMPLETO.keys())

# Álbum del usuario.
# Cada clave representa una sección y el valor asociado es una lista
# con las figuritas obtenidas de esa sección.
album = {seccion: [] for seccion in SECCIONES}


# ==========================================================
# COMPLETE LAS SIGUIENTES FUNCIONES
# ==========================================================

def ingresar_figurita():
    """
    # 10 puntos
    Solicita al usuario una sección y un número de figurita.

    Debe validar que:

    - La sección exista.
    - El número esté dentro del rango de figuritas de cada sección.

    Si alguno de los datos es inválido deberá volver a solicitarlo
    hasta que se ingrese uno válido.


    Retorna:
        (seccion, numero)
    """
    while True:
        seccion = input("Ingrese la sección: ").upper()
        if seccion in SECCIONES:
            break
        print(f"Sección inválida. Las secciones válidas son: {', '.join(sorted(SECCIONES))}")

    while True:
        try:
            numero = int(input("Ingrese el número de figurita: "))
            if numero in ALBUM_COMPLETO[seccion]:
                break
            print(f"Número inválido. Debe estar entre 1 y 39.")
        except ValueError:
            print("Debe ingresar un número entero.")

    return (seccion, numero)


def agregar_figurita():
    """
    # 5 puntos
    Solicita una figurita y la agrega al álbum del usuario.
    """
    seccion, numero = ingresar_figurita()
    album[seccion].append(numero)
    print(f"Figurita {seccion}-{numero} agregada al álbum.")


def mostrar_coleccion():
    """
    # 5 puntos
    Muestra todas las figuritas almacenadas en el álbum.

    Formato esperado:

    ARG: [1, 5, 10]
    BRA: [2, 8]
    ...
    """
    for seccion in sorted(album):
        print(f"{seccion}: {sorted(album[seccion])}")


def mostrar_faltantes():
    """
    # 10 puntos
    Muestra las figuritas que todavía faltan conseguir
    para cada sección.

    Las figuritas deben mostrarse de forma ordenada, de menor a mayor.

    Formato esperado:

    ARG: [1, 5, 10]
    BRA: [2, 8]
    """
    for seccion in sorted(ALBUM_COMPLETO):
        obtenidas = set(album[seccion])
        faltantes = sorted(num for num in ALBUM_COMPLETO[seccion] if num not in obtenidas)
        print(f"{seccion}: {faltantes}")


def buscar_figurita():
    """
    # 5 puntos
    Solicita una figurita y determina si se encuentra en el álbum.

    Debe mostrar:

        Figurita encontrada

    o

        Figurita no encontrada

    según correpsonda.
    """
    seccion, numero = ingresar_figurita()
    if numero in album[seccion]:
        print("Figurita encontrada")
    else:
        print("Figurita no encontrada")


def mostrar_repetidas():
    """
    # 10 puntos
    Muestra todas las figuritas repetidas para cada sección.

    Una figurita está repetida si aparece más de una vez.

    Formato esperado:

    ARG: [1, 5, 10]
    BRA: [2, 8]
    """
    for seccion in sorted(album):
        repetidas = sorted(
            num for num in set(album[seccion])
            if album[seccion].count(num) > 1
        )
        print(f"{seccion}: {repetidas}")



# ==========================================================
# Programa principal
# ==========================================================

if __name__ == "__main__":
    """
    # 10 puntos
    Al iniciar el programa, saludar al usuario.

    Luego, mostrar un menú interactivo donde el usuario puede elegir:

    1 - Agregar figurita
    2 - Mostrar colección
    3 - Mostrar figuritas repetidas
    4 - Mostrar figuritas faltantes
    5 - Buscar figurita
    0 - Salir

    Solicitar al usuario que ingrese una opción.

    Ejecutar la función correspondiente según la opción elegida

    Volver a mostrar el menú hasta que el usuario seleccione la opción 'Salir'.

    Finalizar el programa mostrando un mensaje de despedida

    Si el usuario ingresa una opción inválida, deberá informarlo y volver a mostrar el menú.
    """
    print("¡Bienvenido al álbum de figuritas del Mundial!")

    while True:
        print("\n--- MENÚ ---")
        print("1 - Agregar figurita")
        print("2 - Mostrar colección")
        print("3 - Mostrar figuritas repetidas")
        print("4 - Mostrar figuritas faltantes")
        print("5 - Buscar figurita")
        print("0 - Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_figurita()
        elif opcion == "2":
            mostrar_coleccion()
        elif opcion == "3":
            mostrar_repetidas()
        elif opcion == "4":
            mostrar_faltantes()
        elif opcion == "5":
            buscar_figurita()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor ingrese una opción del menú.")

    print("¡Hasta luego!")