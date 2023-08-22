
def LeeVector(vector, cant): #Creo un procedimiento con los parametros vector(arreglo) y cant(cantidad de elementos para el arreglo)

    for i in range(cant): #Ocupo un ciclo for el cual recorre la cantidad indicada en el parametro

        vector.append(input(f"Ingrese el elemento n°{i+1}: ")) #Hago un append a un input donde el usuario ingresara un elemento

    
def Ordena(vector): # Creo un procedimiento ordena con el parametro vector(Este parametro sirve para ingresar el nombre de tu arreglo y asi poder manipularlo)

    tamaño = len(vector)-1 #Creo una variable de nombre tamaño para guardar el tamaño del vector y le resto 1 para asi usarlo para recorrer el arreglo.
    #Recordar que los arreglos parten de 0 por eso le resto 1

    for i in range(tamaño): #Ocupo un ciclo for el cual recorre la cantidad equivalente al tamaño del arreglo

        naux = vector[i] #Creo una variable auxiliar (naux), para guardar temporalmente el elemento dentro del espacio del arreglo indicado por el indice
        #Con el fin de intercambiar la primera variable con la ultima sin perder la informacion.

        vector[i] = vector[tamaño-i] #Reemplazo la primera variable del arreglo con la ultima variable del arreglo.

        vector[tamaño-i] = naux #Reemplazo la ultima variable del arreglo con el valor que contiene la variable auxiliar
        #la cual contiene el valor la primera variable antes de ser reemplazada.


vector =[] #Inicio una variable tipo lista con el nombre "vector"

LeeVector(vector,2) #Llamo a el procedimiento LeeVector() con sus respectivos parametros

Ordena(vector) #Llamo a el procedimiento Ordenar() Con su respectivo parametro

print("El vector ordenado queda de la siguiente forma") #Imprimo una oracion

print(vector) #Imprimo el arreglo ya manipulado

