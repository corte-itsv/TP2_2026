def min_max(numeros):
    if not numeros:
        return None
    
    minimo = numeros[0]
    maximo = numeros[0]
    
    for num in numeros:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
            
    return minimo, maximo

# Pruebas
numeros = [34, 7, 89, 12, 56, 3, 78, 45]
min_val, max_val = min_max(numeros)

print(f"Mínimo: {min_val}")
print(f"Máximo: {max_val}")