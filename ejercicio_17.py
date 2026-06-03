def cifrar(texto, desplazamiento):
    resultado = ""

    for letra in texto:
        if letra.isalpha():
            resultado += chr(
                (ord(letra) - ord("a") + desplazamiento) % 26
                + ord("a")
            )
        else:
            resultado += letra

    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave = 3

cifrado = cifrar(mensaje, clave)

print("Original:", mensaje)
print("Cifrado:", cifrado)
print("Descifrado:", descifrar(cifrado, clave))