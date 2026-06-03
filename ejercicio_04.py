def min_max(numeros):
    if not numeros:
        return None

    minimo = numeros[0]
    maximo = numeros[0]
    for n in numeros:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    return (minimo, maximo)


if __name__ == "__main__":
    numeros = [34, 7, 89, 12, 56, 3, 78, 45]
    resultado = min_max(numeros)
    if resultado is None:
        print("Lista vacía")
    else:
        minimo, maximo = resultado
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}")
