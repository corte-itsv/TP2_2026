def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha() and letra.islower():
            codigo = chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado += codigo
        else:
            resultado += letra
    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)

mensaje = "hola mundo"
clave = 3

texto_encriptado = cifrar(mensaje, clave)
texto_desencriptado = descifrar(texto_encriptado, clave)

print(f"Original:  {mensaje}")
print(f"Cifrado:   {texto_encriptado}")
print(f"Descifrado: {texto_desencriptado}")