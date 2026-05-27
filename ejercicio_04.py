def min_max(numeros):
    min = numeros[0]
    max = numeros[0]
    for b in numeros:
        if b < min:
            min = b
        if b > max:
            max = b
    return min, max
numeros = [34, 7, 89, 12, 56, 3, 78, 45]
min, max = min_max(numeros)
print(f"El número mínimo es: {min}")
print(f"El número máximo es: {max}")   