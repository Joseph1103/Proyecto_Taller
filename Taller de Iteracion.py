# 8. Utilizando el ciclo while, implemente una funci´on para computar la siguiente sumatoria

def sumatoria_while(N, x):
    resultado = 0
    n = -7

    while(n <= N):
        resultado +=(x**n)/(n+x)

        # incrementar el indice
        n +=1

    print("El resultado de la sumatoria es", resultado)

sumatoria_while(5, 100)

# 9. Utilizando el ciclo for, realice la multiplicacion de 2 vectores (listas de una dimension).


# :c



# 10. Utilizando el ciclo for, realice la suma de la diagonal y la antidiagonal de una matriz
# cuadrada, e imprima ambos resultados.



# :c



# 11. Utilizando cualquier metodo iterativo, retorne la posicion del valor mas alto dentro de una matriz de numeros enteros.
# Retorne el resultado utilizando la notacion
# f ila, columna.

def mayor_matriz(matriz):
    elemento_mayor = 0  # ****
    fila_mayor = 0
    columna_mayor = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):

            # Evaluar si el elemento es mayor a elemento_mayor
            if matriz[fila][columna] > elemento_mayor:
                elemento_mayor = matriz[fila][columna]
                fila_mayor = fila
                columna_mayor = columna
    print("El elemento mayor es {} y esta en la posicion ({}, {})". format(elemento_mayor, fila_mayor, columna_mayor))

mayor_matriz([[1 ,2 , 3], [4, 5, 6],[7, 8, 9]])


# 12. Utilizando cualquier metodo iterativo, hacer una funcion que multiplique los elementos
# de una lista.
# :c




# 13. Utilizando recursividad, hacer una funcion que reciba una lista de numeros y obtenga
# otra solo con los numeros pares.

# :c





