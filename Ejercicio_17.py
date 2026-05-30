def cifrar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            resultado += char
    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave   = 3

cifrado    = cifrar(mensaje, clave)
descifrado = descifrar(cifrado, clave)

print(f"Original:   {mensaje}")
print(f"Cifrado:    {cifrado}")
print(f"Descifrado: {descifrado}")