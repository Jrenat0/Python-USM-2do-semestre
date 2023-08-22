import random


def PromedioAltura(laltura):
    acumulador=0
    for i in range(len(laltura)):
        acumulador+=laltura[i]
    return acumulador/len(laltura)

def PromedioPeso(lpeso):
    acumulador=0
    for i in range(len(lpeso)):
        acumulador+=lpeso[i]
    return acumulador/len(lpeso)


def OrdenarNombres(lnombres,laltura,lpeso):
    for i in range(6):
        for j in range(6):
            if lnombres[i]<lnombres[j]:
                naux = lnombres[i]
                altaux = laltura[i]
                pesoaux = lpeso[i]

                lnombres[i]=lnombres[j]
                laltura[i]=laltura[j]
                lpeso[i]=lpeso[j]

                lnombres[j]=naux
                laltura[j]=altaux
                lpeso[j]=pesoaux


def Mayor(lnombres,laltura,lpeso):
    MasAlto = 0
    alturamax = 0

    MasPesado = 0
    pesomax = 0

    for i in range(6):
        if laltura[i] > alturamax:
            MasAlto = i
            alturamax = laltura[i]

    for i in range(6):
        if lpeso[i] > pesomax:
            MasPesado=i
            pesomax = lpeso[i]

    return print(f"{lnombres[MasAlto]} Es la persona con mas altura y {lnombres[MasPesado]} Es la persona con mas peso.")










#------------------- Main ----------------------------------#
Nombres=[None for i in range(6)]
Altura=[None for i in range(6)]
Peso=[None for i in range(6)]

Nombres[0] = "Joaquin"
Nombres[1] = "Martin"
Nombres[2] = "Benjamin"
Nombres[3] = "Valentin"
Nombres[4] = "Florentin"
Nombres[5] = "Vladimir"

for i in range(6):
    Altura[i] = random.uniform(1,3)
    Peso[i] = random.uniform(15,135)


print(Nombres)

OrdenarNombres(Nombres,Altura,Peso)

print(Nombres)

print(PromedioAltura(Altura))

print(PromedioPeso(Peso))

Mayor(Nombres,Altura,Peso)