def min_max(numeros):
    if not numeros:
        return None, None
    
    minimo = numeros[0]
    maximo = numeros[0]
    
    for num in numeros:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
            
    return (minimo, maximo)


numeros = [34, 7, 89, 12, 56, 3, 78, 45]

val_min, val_max = min_max(numeros)

print(f"Mínimo: {val_min}")
print(f"Máximo: {val_max}")