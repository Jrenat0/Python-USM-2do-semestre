
import random as rd

def ExploraCoordenadas(area, mineraldeseado):

    coordenadas = []

    for filas in range(len(area)):

        for columnas in range(len(area[filas])):

            if area[filas][columnas] == mineraldeseado:

                coordenadas.append([(filas+1), (columnas+1)])

    return print(f"A continuacion se muestran las coordenadas de cada mena: \n{coordenadas}")


def Contador(area, mineraldeseado, mineral):

    contadormineral = 0

    for filas in range(len(area)):

        for columnas in range(len(area[filas])):

            if area[filas][columnas] == mineraldeseado:

                contadormineral+=1

    return print(f"Se encontraron {contadormineral} menas de {mineral}!!")


def RellenarArea(area):

    for filas in range(5):

        area.append([])

        for columnas in range(6):

            generador = rd.randint(1,3)

            if generador == 1:

                area[filas].append('P')

            elif generador == 2:

                area[filas].append('O')

            else:

                area[filas].append('T')


def ElegirMineral():
    mineraldeseado = 0

    while not 0<mineraldeseado<4:

        try:

            mineraldeseado =int(input("Ingrese el mineral deseado\n1.- Plata \n2.-Oro \n3.-Tierra\n==>: "))

        except:

            print("Se esperaba un numero")

        
    if mineraldeseado == 1:

        mineraldeseado = 'P'

        mineral = "Plata"

    elif mineraldeseado == 2:

        mineraldeseado = 'O'

        mineral = "Oro"
    else:

        mineraldeseado = 'T'

        mineral = "Tierra"
    
    return mineraldeseado, mineral

area = []

RellenarArea(area)

print(area)

m1 , m2 = ElegirMineral()

Contador(area, m1, m2)

ExploraCoordenadas(area, m1)
