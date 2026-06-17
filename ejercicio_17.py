def cifrar(texto, desplazamiento):
    texto_cifrado = ""
    for letra in texto:
        if letra.islower():    
            caracter_cif = chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
            texto_cifrado += caracter_cif
        else:
            texto_cifrado += letra
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento):
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra.islower():
            caracter_descif = chr((ord(letra) - ord('a') - desplazamiento) % 26 + ord('a'))
            texto_descifrado += caracter_descif
        else:
            texto_descifrado += letra
    return texto_descifrado

mensaje = "hola mundo"
clave = 3
mensaje_encriptado = cifrar(mensaje, clave)
print(f"Original:  {mensaje}")
print(f"Cifrado:   {mensaje_encriptado}")
print(f"Descifrado: {descifrar(mensaje_encriptado, clave)}")
