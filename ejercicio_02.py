def calcular_promedio(notas):
    if not notas:
        return 0
    promedio = sum(notas) / len(notas)
    return round(promedio, 2)

if __name__ == "__main__":
    lista_a = [8, 9, 7, 10, 6]
    lista_b = [4, 5, 3, 6, 4, 5]
    lista_c = []
    
    print(f"Promedio A: {calcular_promedio(lista_a)}")
    print(f"Promedio B: {calcular_promedio(lista_b)}")
    print(f"Promedio C: {calcular_promedio(lista_c)}")