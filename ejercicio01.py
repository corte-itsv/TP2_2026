def clasificar_nota(nota: int) -> str:
    if nota == 10:
        return "Perfecto"
    elif nota in (8, 9):
        return "Muy bueno"
    elif nota in (6, 7):
        return "Aprobado"
    elif nota in (4, 5):
        return "Desaprobado (cerca)"
    elif nota in (1, 2, 3):
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"


if __name__ == "__main__":
    notas = [10, 7, 4, 0, 11]
    for n in notas:
        print(f"{n} → {clasificar_nota(n)}")
