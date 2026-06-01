def cifrar(texto, desplazamiento):
    texto_cifrado = "" 
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            texto_cifrado += chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento):
    texto_descifrado = ""  
    for caracter in texto_cifrado:
        if 'a' <= caracter <= 'z':
            texto_descifrado += chr((ord(caracter) - ord('a') - desplazamiento) % 26 + ord('a'))
        else:
            texto_descifrado += caracter  
    return texto_descifrado


mensaje = "hola mundo"
clave = 3
mensaje_encriptado = cifrar(mensaje, clave)
print(f"Texto original: {mensaje}")
print(f"Texto cifrado: {mensaje_encriptado}")
print(f"Texto descifrado: {descifrar(mensaje_encriptado, clave)}")