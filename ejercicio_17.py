def cifrar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            codigo = (ord(caracter) - ord("a") + desplazamiento) % 26 + ord("a")
            resultado += chr(codigo)
        else:
            resultado += caracter
    return resultado


def descifrar(texto_cifrado, desplazamiento):
    resultado = ""
    for caracter in texto_cifrado:
        if caracter.isalpha():
            codigo = (ord(caracter) - ord("a") - desplazamiento) % 26 + ord("a")
            resultado += chr(codigo)
        else:
            resultado += caracter
    return resultado


mensaje = "hola mundo"
clave = 3

texto_cifrado = cifrar(mensaje, clave)
texto_descifrado = descifrar(texto_cifrado, clave)

print("Original: ", mensaje)
print("Cifrado:  ", texto_cifrado)
print("Descifrado:", texto_descifrado)