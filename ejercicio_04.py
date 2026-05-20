def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]
    
    for n in numeros:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    
    return minimo, maximo
    
numeros = [34, 7, 89, 12, 56, 3, 78, 45]

minimo, maximo = min_max(numeros) 

print("minimo:", minimo)
print("maximo:", maximo)