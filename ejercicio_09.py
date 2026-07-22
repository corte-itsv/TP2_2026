def agregar_contacto(agenda, nombre, telefono):
    if nombre in agenda:
        return "El contacto ya existe"
    else:
        agenda[nombre] = telefono
        return "Contacto agregado"
    

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return f"{agenda[nombre]}"
    else: 
        return f"Contacto no encontrado"
    

def eliminar_contacto(agenda, nombre): 
    if nombre in agenda: 
        del agenda[nombre] 
        return "Contacto eliminado" 
    else: 
        return "Contacto no encontrado"
    

def mostrar_agenda(agenda): 
    if not agenda: 
        return "La agenda está vacía" 
    contactos = [f"{nombre}: {telefono}" for nombre, telefono in sorted(agenda.items(),
    key=lambda it: it[0].lower())]
    return "\n".join(contactos)


agenda = {}
agregar_contacto(agenda, "Ana",    "351-1234")
agregar_contacto(agenda, "Luis",   "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")


print("=== AGENDA ===")
print(mostrar_agenda(agenda))
print("")
print("Teléfono de Luis:",buscar_contacto(agenda, "Luis"))
print("Pedro:",buscar_contacto(agenda, "Pedro"))
print("")
print("=== AGENDA ===")
eliminar_contacto(agenda, "Marcos")
print(mostrar_agenda(agenda))
