def cifrar(texto, desplazamiento):
    cifrado = ""
    for char in texto:

        if 'a' <= char <= 'z':

            cifrado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:

            cifrado += char
    return cifrado

def descifrar(texto_cifrado, desplazamiento):

    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave = 3
msg_cifrado = cifrar(mensaje, clave)

print(f"Original:  {mensaje}")
print(f"Cifrado:   {msg_cifrado}")
print(f"Descifrado: {descifrar(msg_cifrado, clave)}")