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
        return f"{nombre} Contacto no encontrado"
    

def mostrar_agenda(agenda):
    if len(agenda) == 0:
        return "La agenda está vacía"
    else:
        contactos = [f"{nombre}: {telefono}" for nombre, telefono in sorted(agenda.items(), key=lambda x: x[0])]
        return "\n".join(contactos)


agenda = {}
agregar_contacto(agenda, "Ana",    "351-1234")
agregar_contacto(agenda, "Luis",   "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")


print(mostrar_agenda(agenda))
print(buscar_contacto(agenda, "Luis"))
print(buscar_contacto(agenda, "Pedro"))
print(eliminar_contacto(agenda, "Marcos"))
print(mostrar_agenda(agenda))

