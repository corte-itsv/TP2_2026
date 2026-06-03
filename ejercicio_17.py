def cifrar(texto, desplazamiento):
    resultado = ""

    for letra in texto:
        if letra.isalpha():
            nueva = chr(
                (ord(letra) - ord('a') + desplazamiento) % 26 + ord('a')
            )
            resultado += nueva
        else:
            resultado += letra

    return resultado


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave = 3

texto_cifrado = cifrar(mensaje, clave)
texto_descifrado = descifrar(texto_cifrado, clave)

print("Original: ", mensaje)
print("Cifrado:  ", texto_cifrado)
print("Descifrado:", texto_descifrado)