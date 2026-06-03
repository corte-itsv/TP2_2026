def cifrar(texto, desplazamiento):
    texto_cifrado = "" 
    for caracter in texto:
        caracter_cif = chr(ord(caracter) + desplazamiento)    
        texto_cifrado += caracter_cif
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento):
    texto_descifrado = ""  
    for caracter in texto_cifrado:
        caracter_descif = chr(ord(caracter) - desplazamiento)  
        texto_descifrado += caracter_descif  
    return texto_descifrado

mensaje = "hola mundo"
clave   = 3
mensaje_encriptado = cifrar(mensaje, clave)
print(f"Texto original: {mensaje}")
print(f"Texto cifrado: {mensaje_encriptado}")
print(f"Texto descifrado: {descifrar(mensaje_encriptado, clave)}")