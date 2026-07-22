def cifrar(texto, desplazamiento):
    texto_cifrado = ""
    for letra in texto:
        if letra != " ":
            numero_de_letra = ord(letra)
            numero_de_letra = numero_de_letra + desplazamiento
            letra_del_nuevo_numero = chr(numero_de_letra)
            texto_cifrado = texto_cifrado + letra_del_nuevo_numero
        else:
            texto_cifrado = texto_cifrado + " "
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento):
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra != " ":
            numero_de_letra = ord(letra)
            numero_de_letra = numero_de_letra - desplazamiento
            letra_de_numero = chr(numero_de_letra)
            texto_descifrado = texto_descifrado + letra_de_numero
        else:
            texto_descifrado = texto_descifrado + " "
    return texto_descifrado


mensaje = "hola mundo"
clave = 3

print("===== CIFRADO CÉSAR =====")

print("Mensaje original:", mensaje)

mensaje_cifrado = cifrar(mensaje, clave)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar(mensaje_cifrado, clave)
print("Mensaje descifrado:", mensaje_descifrado)
