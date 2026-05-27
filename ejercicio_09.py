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
    for nombre, telefono in sorted(agenda.items()):
        print(f"{nombre}: {telefono}")

agenda = {}
agregar_contacto(agenda, "Ana", "351-1234")
agregar_contacto(agenda, "Luis", "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")

mostrar_agenda(agenda)
print(f"\nTeléfono de Luis: {buscar_contacto(agenda, 'Luis')}")
print(f"Pedro: {buscar_contacto(agenda, 'Pedro')}")
eliminar_contacto(agenda, "Marcos")
print()
mostrar_agenda(agenda)