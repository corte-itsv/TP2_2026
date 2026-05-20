notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

aprobados = 0
desaprobados = 0

def contar_aprobados(notas):
    for aprobados in len(notas):
        if nota >= 6:
            aprobados = aprobados + 1
        else:
            aprobados = aprobados + 0
    
def contar_desaprobados(notas):
    for desaprobados in len(notas):
        if nota <= 5:
            desaprobados = desaprobados + 1
        else:
            desaprobados =  desaprobados + 0

cant_aprobados = contar_aprobados(notas)
cant_desaprobados = contar_desaprobados(notas)

print(cant_aprobados)
print(cant_desaprobados)