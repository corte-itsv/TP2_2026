def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num) 
    return pares  

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f"Versión A: {filtrar_pares(numeros)}")
print(f"Versión B: {filtrar_pares(numeros)}")