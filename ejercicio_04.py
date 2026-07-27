def min_max(numeros):
    numero_minimo = numeros[0]
    numero_maximo = numeros[0]
    for numero in numeros:
        if numero < numero_minimo:
            numero_minimo = numero
        if numero > numero_maximo:
            numero_maximo = numero
    return (numero_minimo, numero_maximo)
            

numeros = [34, 7, 89, 12, 56, 3, 78, 45]
print("=== MÍN-MÁX ===")

minimo, maximo = min_max(numeros)
print("Numero Mínimo:", minimo)
print("Numero Máximo:", maximo)