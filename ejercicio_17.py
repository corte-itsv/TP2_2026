def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if 'a' <= letra <= 'z':
            codigo = (ord(letra) - ord('a') + desplazamiento) % 26 + ord('a')
            resultado += chr(codigo)
        else:
            resultado += letra
    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)

mensaje = "hola mundo"
clave = 3

mensaje_cifrado = cifrar(mensaje, clave)
mensaje_descifrado = descifrar(mensaje_cifrado, clave)

print(f"Original: {mensaje}")
print(f"Cifrado: {mensaje_cifrado}")
print(f"Descifrado: {mensaje_descifrado}")
