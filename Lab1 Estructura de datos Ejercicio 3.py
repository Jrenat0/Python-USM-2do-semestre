def nombrecompleto():
    nombre=None #Creo la variable nombre para posteriormente guardar el nombre ingresado.
    apellidop=None #Creo la variable nombre para posteriormente guardar el Apellido Paterno ingresado.
    apellidom=None #Creo la variable nombre para posteriormente guardar el Apellido Materno ingresado.

    while nombre==None:  #Hago un while que funcione mientra la variable nombre siga en None.

        nombrecompleto=input("Porfavor ingrese su nombre, su apellido paterno y su apellido materno separando cada uno de ellos con un espacio: ")
        #Creo la variable nombre completo para despues hacer un input y rellenarla con los datos correspondientes.

        partes=nombrecompleto.split()
        #Hago la variable partes y ocupo la funcion split la cual divide un string en partes guiandose por los espacios vacios en el texto.

        if len(partes) == 3:   #Pregunto en cuantas partes se dividio el texto de la variable nombre completo.

            #Si hay exactamente 3 partes entonces el programa viene por aqui.
            nombre = partes[0]
            apellidop= partes[1]
            apellidom= partes[2] 

        else: #Si hay mas de 3 partes o menos de 3 partes el programa se va por aqui.

            print("Formato incorrecto, porfavor ingrese su nombre, su apellido paterno y su apellido materno separandolos con un espacio!!")
    
    nombreformato = f"{apellidop} {apellidom} {nombre}" #Hago la variable nombre formato donde guardo el nombre completo con el formato indicado.

    print(f"El nombre ingresado es: {nombreformato}") #Imprimo el nombre con el formato nuevo.

    return nombre, apellidop, apellidop #No tomar en cuenta esto porque es innecesario.

nombrecompleto()