
def min_max(numeros):

 minimo = numeros[0]
 maximo = numeros[0]

 for num in numeros:
  if num < minimo:
   minimo = num
  if num > maximo:
   maximo = num

 return (minimo, maximo)



Numeros = [34, 7, 89, 12, 56, 3, 78, 45]
minimo, maximo = min_max(Numeros)

print("Mínimo:", minimo)
print("Máximo:", maximo)

