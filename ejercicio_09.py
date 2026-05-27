def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono


def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return "Contacto no encontrado"


def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]


def mostrar_agenda(agenda):
    print("=== AGENDA ===")

    for nombre in sorted(agenda):
        print(nombre, "-", agenda[nombre])


# Crear agenda
agenda = {}

# Agregar contactos
agregar_contacto(agenda, "Ana", "351-1234")
agregar_contacto(agenda, "Luis", "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")


# 1. Mostrar agenda completa
mostrar_agenda(agenda)

# 2. Buscar a "Luis"
print("\nBuscar Luis:", buscar_contacto(agenda, "Luis"))

# 3. Buscar a "Pedro"
print("Buscar Pedro:", buscar_contacto(agenda, "Pedro"))

# 4. Eliminar a "Marcos"
eliminar_contacto(agenda, "Marcos")

# 5. Mostrar agenda final
print("\nAgenda final:")
mostrar_agenda(agenda)