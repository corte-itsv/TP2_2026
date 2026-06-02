def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():  
            nueva = chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado += nueva
        else:
            resultado += letra  
    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)



mensaje = "hola mundo"
clave   = 3

cifrado = cifrar(mensaje, clave)
descifrado = descifrar(cifrado, clave)

print("Original:  ", mensaje)
print("Cifrado:   ", cifrado)
print("Descifrado:", descifrado)
