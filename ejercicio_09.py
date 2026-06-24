agenda = {}
def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono

def buscar_contacto(agenda, nombre_a_encontrar):
    for nombre in agenda:
        if nombre == nombre_a_encontrar:
            return agenda[nombre]
    return "Contacto no encontrado"
        
def eliminar_contacto(agenda, nombre_a_eliminar):
    resultado_de_busqueda = buscar_contacto(agenda, nombre_a_eliminar)
    if resultado_de_busqueda != "Contacto no encontrado":
        agenda.pop(nombre_a_eliminar)
    
def mostrar_agenda(agenda):
    for nombre in agenda:
        if nombre in agenda:
            print(nombre, ": ", agenda[nombre])
        else: print("")


print("=== AGENDA ===")

agregar_contacto(agenda, "Ana", "351-1234")
agregar_contacto(agenda, "Luis", "351-5678")
agregar_contacto(agenda, "Marcos", "351-9012")


mostrar_agenda(agenda)
print("")
buscar_contacto(agenda, "Ana")
buscar_contacto(agenda, "Luis")
buscar_contacto(agenda, "Marcos")

resultado_de_busqueda = buscar_contacto(agenda, "Luis")
print("Telefono de Luis: ", resultado_de_busqueda)

resultado_de_busqueda = buscar_contacto(agenda, "Pedro")
print("Pedro: ", resultado_de_busqueda)


eliminar_contacto(agenda, "Marco")

print("")
print("=== AGENDA ===")
mostrar_agenda(agenda)








