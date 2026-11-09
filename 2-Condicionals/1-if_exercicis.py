###
# EXERCICIS
###
import os
os.system("cls") 

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivell_senyal = float(input("Introdueix el nivell de senyal rebut (dBm): "))
if nivell_senyal>= -50:
    print("Excel·lent\n")
elif nivell_senyal>=-67:
    print("Bona\n")
elif nivell_senyal>=-75:
    print("Feble")
else:
    print("Molt feble\n")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
nivell_connexió = float(input("Introdueix el nilvell de connexió de fibra òptica: "))
if nivell_connexió > -8:
    print("Massa alt\n")
elif nivell_connexió>= -27:
    print("Acceptable\n")
else:
    print("Massa baix\n")


# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum mensual de dades mòbils: "))
if consum>20:
    print(f"S'ha superat el límit en {consum-20} GB\n")
else:
    print("Consum dins del límit\n")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los_ences = input("L'indicador LOS està encès? (sí/no): ").lower().strip() == "sí"
internet_ences = input("L'indicador d'Internet està encès? (sí/no): ").lower().strip() == "sí"

if los_ences:
    print("Cal revisar el cable de fibra.\n")
elif not internet_ences:
    print("Cal comprovar el servei del proveïdor.\n")
else:
    print("La connexió sembla funcionar correctament.\n")


# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = int(input("Introdueix el percentatge de bateria: "))
if bateria>100 or bateria<0:
    printf("Valor fora de rang")
else:
    if bateria >= 50:
        print("Suficient")
    elif bateria >= 20:
        print("baix")
    else:
        print("Crític") 

