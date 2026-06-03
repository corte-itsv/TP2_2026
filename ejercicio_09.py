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


agenda = {}
agregar_contacto(agenda, "Ana",    "351-1234")
agregar_contacto(agenda, "Luis",   "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")

mostrar_agenda(agenda)
print()
print(f"Teléfono de Luis: {buscar_contacto(agenda, 'Luis')}")
print(f"Pedro: {buscar_contacto(agenda, 'Pedro')}")
print()
eliminar_contacto(agenda, "Marcos")
mostrar_agenda(agenda)