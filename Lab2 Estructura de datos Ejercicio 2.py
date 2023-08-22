def raiz2 (n): # Creo una funcion para calcular la raiz cuadrada con el parametro N el cual es el numeroo al cual se desea aplicar la raiz cuadrada.
    xant = n/2
    encontrado = False
    while encontrado != True:
        xnuevo = (1/2)*(xant + (n/xant))
        print(xant, xnuevo)
        if abs((xnuevo - xant)) <= 10**-6:
            encontrado = True
        else:
            xant = xnuevo

raiz2(25)