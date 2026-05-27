def contar_aprobados(notas):
    contador = 0
    for nota in notas:
        if nota >= 6:
            contador += 1
    return contador

def contar_desaprobados(notas):
    contador = 0
    for nota in notas:
        if nota < 6:
            contador += 1
    return contador

if __name__ == "__main__":
    notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
    
    print(f"Total: {len(notas)} alumnos")
    print(f"Aprobados: {contar_aprobados(notas)}")
    print(f"Desaprobados: {contar_desaprobados(notas)}")


