def clasificar_nota(nota):
    if nota == 10:
      return "Perfecto"
    elif nota in [9, 8]:
      return "Muy bueno"
    elif nota in [6, 7]:
       return "aprobado"
    elif nota in [4, 5]:
       return "Desaprobado (cerca)"
    elif nota in [1, 2, 3]:
       return "Desaprobado (lejos)"
    else: 
       return "Nota inválida"
       
       
notas_a_probar = [10, 7, 4, 0, 11]
for n in notas_a_probar:
    resultado = clasificar_nota(n)
    print(f"Nota: {n} -> Clasificación: {resultado}")
