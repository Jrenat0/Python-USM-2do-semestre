import random 


def llenarmatriz(matriz,f=1,c=1): #matriz es para ingresar la lista donde se creara la matriz, f equivale a filas, c equivale a columnas.

    for filas in range(f):  #Recorro las filas en el rango "f" el cual indica el programador.

        matriz.append([])  #Agrego una sublista a cada fila con el fin de recrear las columnas.

        for columnas in range(c): #Recorro las columnas en el rango "c" el cual indica el programador.

            elemento = random.randint(1,100) #Genero un elemento aleatorio con randint.

            matriz[filas].append(elemento) #Hago un append del numero aleatorio con matriz[filas].append para agregar el dato a la fila correspondiente. 

def sumarmatriz(matriz): #matriz es para ingresar la lista donde se creara la matriz.

    suma=0 #acumulador del total de la suma de todos los argumentos de la matriz.

    for filas in matriz: #recorro cada fila en la matriz con un for.

        for columnas in filas:  #recorro cada columna en la fila con un for.

            suma+=columnas        #sumo al acumulador el valor que se encuentra en esa posicion de la matriz.
    
    print(f"La suma total de la matriz es de: {suma}")

    return suma #Devuelvo la variable suma para su manipulacion.

def sumardiagonal(matriz): #matriz es para ingresar la lista donde se creara la matriz.

    diagonal=0 #acumulador del total de la suma de la diagonal de la matriz

    for i in range(len(matriz)): # hago una variable i que recorra una cantidad de veces equivalente al tamaño de la matriz

        diagonal+=matriz[i][i]   # sumo al acumulador los valores correspondientes a la diagonal, usando el mismo numero en la columna y en la fila (lista[i][i])
    

    print(f"La suma de la diagonal principal de la matriz es de: {diagonal}")

    return diagonal #devuelvo el acumulador

def sumardiagonalsecun(matriz): #matriz es para ingresar la lista donde se creara la matriz.

    diagonal2=0 #acumulador del total de la suma de la diagonal secundaria de la matriz

    t=len(matriz) # asigno el valor del tamaño de la lista a una variable(t por tamaño)

    for i in range(t): # recorro el tamaño de la lista con la variable i.

        diagonal2+=matriz[i][t-1-i] #sumo al acumulador los valores correspondientes a la diagonal secundaria.

        #la diagonal secundaria tiene la particularidad de cuando un eje aumenta, el otro disminuye proporcionalmente. ej [1][4],[2][3],[3][2],etc.

        #por eso a t(tamaño) le voy restando i, para que cuando i aumente, t disminuya.

        #tambien le resto 1 a t debido a q el tamaño de la matriz es cuatro, pero estas se trabajan contando el 0 por lo que el 4 no existe en este caso.

    
    print(f"La suma de la diagonal secundaria de la matriz es de: {diagonal2}")

    return diagonal2 #devuelvo el acumulador

def mostrarmatriz(matriz): #matriz es para ingresar la lista donde se creara la matriz.

    for filas in matriz: #Recorro las filas de la matriz y las imprimo.
        print(filas)

def sumarfila(matriz): #matriz es para ingresar la lista donde se creara la matriz.

    fila=0  #creo una variable para guardar el numero de la fila ingresado por el usuario y lo inicializo en cero para empezar un while.

    suma=0  #creo un acumulador para la suma de los valores en la fila seleccionada

    while fila<1 or fila>len(matriz): #hago un while que funcione hasta que el numero ingresado sea mayor a 0 y menor o igual al tamaño de la matriz.
        try:
            fila=int(input("Ingrese el numero de la fila que quiere sumar: "))

            if fila<1 or fila>len(matriz): #Si el numero ingresado no entra en el rango, le indico al usuario cual es el rango.

                print(f"Porfavor ingrese un numero entre 1 y {len(matriz)}")

        except:

            print("Se esperaba un numero entero!!") #si el usuario ingresa un tipo de dato erroneo, le indico que tipo de dato se espera.

    for columnas in matriz[fila-1]: #recorro cada argumento dentro de la fila indicada por el usuario. (le resto 1 a fila ya que las listas parten de 0)

        suma+=columnas #sumo cada argumento de la fila al acumulador

    print(f"La suma total de los valores de la fila n°{fila} es de: {suma}")
    
    return suma


listamatriz = [] #Creo una lista para poder recrear una matriz

llenarmatriz(listamatriz, f=4, c=4) 
#Ocupo la funcion llenarmatriz para crear la matriz y llenarla segun las dimensiones especificadas. f equivale a las filas y c equivale a las columnas.

mostrarmatriz(listamatriz)
#Ocupo la funcion mostrarmatriz para mostrar la matriz de la manera correcta.

sumarmatriz(listamatriz)
#Ocupo la funcion sumarmatriz para sumar el total de los valores de la matriz.

sumardiagonal(listamatriz)
#Ocupo la funcion sumardiagonal para sumar la diagonal principal de la matriz.

sumardiagonalsecun(listamatriz)
#Ocupo la funcion sumardiagonalsecun para sumar la diagonal secundaria de la matriz.

sumarfila(listamatriz)


