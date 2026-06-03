def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha() and letra.islower():
            nueva = chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado += nueva
        else:
            resultado += letra
    return resultado


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


# Prueba
mensaje = "hola mundo"
clave   = 3

cifrado    = cifrar(mensaje, clave)
descifrado = descifrar(cifrado, clave)

print(f"Original:   {mensaje}")
print(f"Cifrado:    {cifrado}")
print(f"Descifrado: {descifrado}")