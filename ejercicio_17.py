def cifrar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha() and caracter.islower():
            nueva_letra = chr(
                (ord(caracter) - ord('a') + desplazamiento) % 26
                + ord('a')
            )
            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


# Prueba
mensaje = "hola mundo"
clave = 3

mensaje_cifrado = cifrar(mensaje, clave)
mensaje_original = descifrar(mensaje_cifrado, clave)

print("Mensaje original :", mensaje)
print("Mensaje cifrado  :", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_original)