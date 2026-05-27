def min_max(numeros):
    if not numeros:
        return(None, None)
    
    minimo = numeros[0]
    maximo = numeros[0]
    
    for numero in numeros:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
          maximo = numero
    return(minimo, maximo)

numeros = [34, 7, 89, 12, 56, 3, 78, 45]

val_min, val_max = min_max(numeros)
print(f"minimo: {val_min}")
print(f"maximo: {val_max}")
