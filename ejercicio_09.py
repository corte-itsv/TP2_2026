agenda = {}

def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    return (nombre, telefono)

def buscar_contacto(agenda, nombre_a_ingresar):
    if nombre_a_ingresar in agenda:
        for nombre, telefono in agenda.items():
            if nombre == nombre_a_ingresar:
                return nombre
                
    else:
        return nombre

def eliminar_contacto(agenda, nombre):
    del agenda[nombre]

def mostrar_agenda(agenda):
    for nombre, telefono in agenda.items():
        print(f"{nombre:<6} : {telefono}")


print("==== AGENDA ====")

nombre, telefono = agregar_contacto(agenda, "Ana",    "351-1234")
print(f"{nombre:<6}: {telefono}")
nombre, telefono = agregar_contacto(agenda, "Luis",   "351-5678")
print(f"{nombre:<6}: {telefono}")
nombre, telefono = agregar_contacto(agenda, "Marcos", "351-9012")
print(f"{nombre:<6}: {telefono}")

print("")

contacto_buscado = buscar_contacto(agenda, "Luis")
print(f"Teléfono de {contacto_buscado}: {telefono}")
contacto_buscado = buscar_contacto(agenda, "Pedro")
print(f"{contacto_buscado}: Contacto no encontrado")

print("")

eliminar_contacto(agenda, "Marcos")


print("==== AGENDA ====")

mostrar_agenda(agenda)