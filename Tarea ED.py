
class pieza():
    def __init__ (self):

        self.NPieza : int #Numero de pieza
        self.Capacidad : int #Capacidad de la pieza
        self.Valorxdia : int #Valor de la pieza x dia
        self.Estado : str #Estado de la pieza 'S' o 'N'

class reserva ():
    def __init__(self):
        self.npieza : int #Numero Pieza
        self.npasajero : str #Nombre pasajero
        self.fingreso : float #Fecha de ingreso
        self.consumo : float #Consumo de cosas extras


arreglohotel = [pieza() for i in range(20)]
with open('Pieza.txt','rt') as f:
    infopiezas = f.readlines()
    f.close

for i in range (len(arreglohotel)):
    piezaaux = infopiezas.split(';')
    arreglohotel[i].NPieza = piezaaux[0]
    arreglohotel[i].Capacidad = piezaaux[1]
    arreglohotel[i].Valorxdia = piezaaux[2]
    arreglohotel[i].Estado = piezaaux[3]

