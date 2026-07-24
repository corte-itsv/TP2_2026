def min_max(numeros):
    
    minimo = numeros[0]
    maximo = numeros[0]
    
    for numero in numeros:
        if minimo > numero:
            minimo = numero
        if maximo < numero:
            maximo = numero
    return (minimo, maximo)

numeros = [34, 7, 89, 12, 56, 3, 78, 45]

menor, mayor = min_max(numeros)

print("Mínimo:", menor)
print("Máximo:", mayor)