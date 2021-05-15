#Tarea de recursividad de cola
#Joseph Coronado Alvarado, Daniel Vargas

#1Escriba una funcion que reciba un numero (que debe ser entero) y retorne dos listas,
#una con los dıgitos entre 0 y 4 y otra con los dıgitos entre 5 y 9.

def lista_split(num):
    if(isinstance(num, int)):
        return lista_split_aux(num, [], [])
    else:
        print("El numero debe ser entero")

def lista_split_aux(num, lista_0_4, lista_5_9):
        if (num==0):
            return lista_0_4, lista_5_9
        else:
            digito = num%10

            if (digito <=4):
                lista_0_4.append(digito)
            else:
                lista_5_9.append(digito)
            return lista_split_aux(num//10, lista_0_4, lista_5_9)

#print(lista_split(123456789))

#2. Construya una funcion de nombre split(lista). Esta funcion toma una lista y la divide
#en sublistas usando como punto de corte cada vez que aparezca un cero.
def split(lista):
    if (isinstance(lista, list)):
        return split_aux(lista, [], [])
    else:
        return "Lista no valida"
def  split_aux(listas, lista_aux, resultado):
    if(listas==[]):
        resultado.append(lista_aux)
        return resultado
    elif(listas[0]!=0):
        lista_aux.append(listas[0])
        return split_aux(listas[1:], lista_aux, resultado)
    else:
        resultado.append(lista_aux)
        return split_aux(listas[1:], [], resultado)

#print(split([1,2,3,0,4,5,6,0,7,8,9]))

#3. Escriba una funcion cambie todos(num) que reciba una numero entero y sustituya
#todos los valores que aparezcan 2 o mas veces por un cero.
def cambie_todos(num):
    if(isinstance(num, int)):
        return cambie_todos_aux(num, repetidos_aux(num, [], []), 0, 0)
    else:
        return "Introduzca numeros validos"

def repetidos_aux(num, digitos, resultado):
    if(num == 0):
        if(digitos == []):
            return resultado
        elif(digitos[0] in digitos [1:]):
            if(digitos[0] in resultado):
                return repetidos_aux(num, digitos[1:], resultado)
            else:
                return repetidos_aux(num, digitos[1:], resultado + [digitos[0]])
        else:
            return repetidos_aux(num, digitos[1:], resultado)
    else:
        digitos.append(num%10)
        return repetidos_aux(num//10, digitos, resultado)

def cambie_todos_aux(num, contar, repetidos, resultado):
    if(num == 0):
        return resultado
    elif(num%10 in repetidos):
        return cambie_todos_aux(num//10, repetidos, contar +1, resultado)
    else:
        return cambie_todos_aux(num//10, repetidos, contar +1, resultado + (num%10)*10**contar)
#print(cambie_todos(1223445677889))


#4. Escriba una funcion coincide(lista) que recibe una lista de numeros enteros e indique
#si algun elemento de la lista coincide con la suma de todos los que le preceden:

def coincide(lista):
    if isinstance(lista, list):
        return coincide_aux(lista, lista[0], 1)
    else:
        return -1
def coincide_aux(lista, r, i):
    print(r)
    if i == len(lista):
        return False
    elif r == lista[i]:
        return True
    else:
        r += lista[i]
        return coincide_aux(lista, r, i+1)
#print(coincide([2,3,4,9,14]))


