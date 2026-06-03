def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    return "Contacto no encontrado"

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]

def mostrar_agenda(agenda):
    print("=== AGENDA ===")
    for nombre in sorted(agenda):
        print(f"{nombre}: {agenda[nombre]}")
    print()


# Datos iniciales
agenda = {}

agregar_contacto(agenda, "Ana", "351-1234")
agregar_contacto(agenda, "Luis", "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")

# Mostrar la agenda completa
mostrar_agenda(agenda)

# Buscar a Luis
print("Teléfono de Luis:", buscar_contacto(agenda, "Luis"))

# Buscar a Pedro
print("Pedro:", buscar_contacto(agenda, "Pedro"))
print()

# Eliminar a Marcos
eliminar_contacto(agenda, "Marcos")

# Mostrar la agenda final
mostrar_agenda(agenda)