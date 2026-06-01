def cifrar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            nueva = chr(
                (ord(caracter) - ord('a') + desplazamiento)
                % 26 + ord('a')
            )
            resultado += nueva
        else:
            resultado += caracter

    return resultado


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave = 3

cifrado = cifrar(mensaje, clave)
descifrado = descifrar(cifrado, clave)

print("Original:", mensaje)
print("Cifrado:", cifrado)
print("Descifrado:", descifrado)