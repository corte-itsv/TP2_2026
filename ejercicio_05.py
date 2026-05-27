def filtrar_pares_a(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

def filtrar_pares_b(numeros):
    return [num for num in numeros if num % 2 == 0]

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    print(f"Versión A: {filtrar_pares_a(numeros)}")
    print(f"Versión B: {filtrar_pares_b(numeros)}")