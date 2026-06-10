def cifrar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord("A") if caracter.isupper() else ord("a")
            resultado += chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            resultado += caracter
    return resultado        


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


mensaje = "hola mundo"
clave   = 3

print(f"Original: {mensaje}")
print(f"Cifrado: {cifrar(mensaje, clave)}")
print(f"Descifrado: {descifrar(cifrar(mensaje, clave), clave)}")