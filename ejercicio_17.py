def cifrar(texto, desplazamiento):
    texto_cifrado = "" 
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            caracter_cif = chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            caracter_cif = caracter
        texto_cifrado += caracter_cif
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento):
    texto_descifrado = ""  
    for caracter in texto_cifrado:
        if 'a' <= caracter <= 'z':
            caracter_descif = chr((ord(caracter) - ord('a') - desplazamiento) % 26 + ord('a'))
        else:
            caracter_descif = caracter  
        texto_descifrado += caracter_descif  
    return texto_descifrado


mensaje = "hola mundo"
clave   = 3
mensaje_encriptado = cifrar(mensaje, clave)
print(f"Texto original: {mensaje}")
print(f"Texto cifrado: {mensaje_encriptado}")
print(f"Texto descifrado: {descifrar(mensaje_encriptado, clave)}")