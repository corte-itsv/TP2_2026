
def contar_aprobados(notas): 
   aprobados = 0
   for notas in notas:
    if notas >= 6:
      aprobados = aprobados + 1
   return aprobados

def contar_desaprobados(notas):
  desaprobados = 0
  for notas in notas:
    if notas < 6:
      desaprobados = desaprobados + 1 
  return desaprobados
    
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

total = len(notas)
desaprobados = contar_desaprobados(notas)
aprobados = contar_aprobados(notas)

print("total:", total)
print("aprobados:", aprobados)
print("aprobados:" ,desaprobados)