

def encontrarmonto():
    #Texto de ejemplo para la funcion
    texto = "El Sr. Felipe Sartori aporta al proyecto $700000 y el Sr. Alejandro Aliaga aporta $550000."

    #Ocupo la funcion find para guardar el indice del primer signo dinero del texto
    signodinero1 = texto.find("$")
    signodinero2 = texto.rfind("$")

    valor1 = texto[signodinero1 + 1 : signodinero1 + texto[signodinero1: ].find(" ")]
    valor2 = texto[signodinero2 + 1 : signodinero2 + texto[signodinero2: ].find(".")]

    valor1aux = valor1
    valor2aux = valor2

    total = int(valor1) + int(valor2)

    valor1=('{:,}'.format(int(valor1)).replace(',','.'))
    valor2=('{:,}'.format(int(valor2)).replace(',','.'))
    total=('{:,}'.format(total)).replace(',','.')

    texto=texto.replace(valor1aux, valor1)
    texto=texto.replace(valor2aux, valor2)

    texto+= f" La suma de ambos corresponde a ${total}"
    
    print(texto)

encontrarmonto()