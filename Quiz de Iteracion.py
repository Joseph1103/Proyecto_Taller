# Joseph Coronado Alvarado
# Primer Ejercicio
# 1. En una lista se reciben las notas de n estudiantes de un curso. Escriba una funci´on
# notas(lista) que, considerando que la nota de aprobaci´on sea 70, obtenga en una lista:
# (a) Cu´antos estudiantes aprobaron el curso.
# (b) Cu´antos estudiantes reprobaron.
# (c) El promedio de notas.

def notas(lista):
    promedio = 0
    cantidad = 0
    aprobados = 0
    aplazados = 0
    for i in lista:
        if i < 70:
            aplazados += 1
            promedio += i
            cantidad +=1
        else:
            aprobados += 1
            promedio += i
            cantidad += 1

    return [round(promedio/cantidad),aprobados, aplazados]
print(notas([10, 20, 25, 25, 30, 40, 100]))



# Segundo Ejercicio
# 2. Escriba una funci´on triangulo(lineas) que genere un tri´angulo de aster´ıscos con la siguiente forma:
#     ∗
#    ∗ ∗
#   ∗ ∗ ∗
#  ∗ ∗ ∗ ∗
#  ∗ ∗ ∗ ∗ ∗
# ∗ ∗ ∗ ∗ ∗ ∗
# donde el argumento de entrada lineas corresponda a la cantidad de l´ıneas que se desea
# imprimir del tri´angulo.
def triangulo(lineas):
   for i in range(lineas):
       print(" " * (lineas - i -1)+"*" * (2 * i + 1))

triangulo(6)
