class pieza():
    def __init__ (self):

        self.NPieza : int #Numero de pieza
        self.Capacidad : int #Capacidad de la pieza
        self.Valorxdia : int #Valor de la pieza x dia
        self.Estado : str #Estado de la pieza 'S' o 'N'


aHotel = [pieza() for ñ in range(15)]

def iniciarsistema(narreglo): #narreglo es para indicar el nombre del arreglo y asi permitir el correcto funcionamiento del proceso 'iniciarsistema'
    with open('Piezas.txt') as f: 
        i = 0
        for registro in f:
            print(registro)
            datos = registro.strip().split(';')
            aHotel[i].NPieza = int(datos[0])
            aHotel[i].Capacidad = int(datos[1])
            aHotel[i].Valorxdia = int(datos[2])
            aHotel[i].Estado = datos[3]
            i+=1



def buscarhabitacion(narreglo):
    encontrado = False
    
    while encontrado==False:
        try:
            capacidadr = int(input("Ingrese la capacidad requerida por el cliente: "))
            if  1<=capacidadr<=3:
                encontrado=True
                
            else:
                print('Porfavor ingrese una capacidad minima de 1 o maxima de 3!!')
        except:
            print('Ingrese un numero entero porfavor!!')
     
        
    for i in range(len(narreglo)):
         if narreglo[i].Estado == 'N':
             if capacidadr <= narreglo[i].Capacidad:
                 print(f'La pieza numero {narreglo[i].NPieza} esta disponible!!')
                 return narreglo[i].NPieza
             
    return False
                
        
        
def registrarpasajero(narreglo):
    
    piezadisponible = buscarhabitacion(aHotel)
    
    if piezadisponible != False:
        
        for i in range(len(narreglo)):
            
            if narreglo[i].NPieza == piezadisponible:
                
               numpieza = narreglo[i].NPieza
               
               nombreP = input("Ingrese el nombre del pasajero: ")
               
               fechaing = int(input("Ingrese la fecha de ingreso: "))
               
               consumo = int(input("Ingrese el consumo del cliente: "))
               
               datos = "{np}{nombre} {fi}{c}".format(np=numpieza,nombre=nombreP,fi=fechaing,c=consumo)
               
               with open('Estadia.txt','w+') as f:
                   
               
               
    
    else:
        print('No se encontró pieza disponible para el registro!!')
        




iniciarsistema(aHotel)

registrarpasajero(aHotel)






