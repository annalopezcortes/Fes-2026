###
# EXERCICIS (mòduls)
# Resol cada exercici en aquest fitxer amb els mòduls auxiliars facilitats.
# Executa des de l'arrel: python 08_moduls/01_moduls_exercicis.py
###

# Exercici 1 - Bàsic. Magnitud d'una mesura
# Importa math amb l'àlies matematiques. Calcula el mòdul d'un vector de
# components x i y amb sqrt(x * x + y * y).
# Entrada: x = 3.0, y = 4.0. Sortida esperada: 5.0.
# Cas límit: x = 0.0, y = 0.0 ha de donar 0.0.
x = 3.0
y = 4.0
# TODO: escriu les importacions i els càlculs.
import math as matematiques
print(matematiques.sqrt(x * x + y * y))
print(matematiques.sqrt(0 * 0 + 0 * 0))

# Exercici 2 - Bàsic. Conversions reutilitzables
# Importa conversions amb l'àlies conv i utilitza les seves funcions.
# Converteix cada temperatura a kelvins i cada tensió a volts.
# Entrades següents. Sortides esperades en el mateix ordre:
# [263.15, 273.15, 298.15] i [0.0, 3.3, 5.0].
# Amb una llista buida, el resultat corresponent ha de ser [].
import conversions as conv
temperatures = [-10.0, 0.0, 25.0]
tensions_mv = [0, 3300, 5000]
temperatures_k = []
tensions_v = []
# TODO: obtén i mostra dues llistes amb les conversions.
for temperatura in temperatures:
    temperatures_k.apend(conv.celsius_a_kelvin(temperatura))
for tension in tensions_mv:
    tensions_v.apend(conv.milivolts_a_volts(tension))

# Exercici 3 - Intermedi. Resum d'una xarxa de sensors
# Importa únicament mitjana del mòdul sensors.
# Crea un diccionari de mitjanes amb els mateixos identificadors que dades.
# Sortida esperada: {'T1': 21.0, 'T2': 18.0, 'T3': None}.
# El mòdul sensors ja defineix el tractament de la llista buida.
from sensors import mitjana 
dades = {"T1": [20.0, 22.0], "T2": [18.0], "T3": []}
# TODO: reutilitza la funció importada per a cada sensor.
mitjanes = {}
for identificador, llista in dades.items():
    mitjanes[identificador] = mitjana(llista)
print(mitjanes)

# Exercici 4 - Repte opcional. Un programa reutilitzable
# Defineix informe_sensor(nom, lectures) que retorni un diccionari amb
# les claus 'nom', 'nombre' i 'mitjana'. Reutilitza sensors.mitjana.
# Entrada: informe_sensor('T1', [20.0, 22.0]).
# Retorn esperat: {'nom': 'T1', 'nombre': 2, 'mitjana': 21.0}.
# Cas límit: informe_sensor('T0', []) ha de retornar
# {'nom': 'T0', 'nombre': 0, 'mitjana': None}.
# Afegeix una funció main() que mostri aquests dos informes.
# Protegeix TOTES les demostracions del fitxer amb __name__ == '__main__'.
# En importar el fitxer no s'ha de mostrar cap sortida.
# TODO: reorganitza les demostracions dels exercicis 1–3 dins de main().
def informe_sensor(nom, lectures): # Resum de tot el que s'ha fet
    return {'nom': nom, 'nombre': len(lectures), 'mitjana': mitjana(lectures)}


# Afegeix una funció main() que mostri aquests dos informes.
def main():
    x = 3.0
    y = 4.0
    print(matematiques.sqrt(x * x + y * y))
    print(matematiques.sqrt(0 * 0 + 0 * 0))



    temperatures = [-10.0, 0.0, 25.0]
    tensions_mv = [0, 3300, 5000]
    temperatures_k = []
    tensions_v = []
    for temperatura in temperatures:
        temperatures_k.apend(conv.celsius_a_kelvin(temperatura))
    for tension in tensions_mv:
        tensions_v.apend(conv.milivolts_a_volts(tension))



    dades = {"T1": [20.0, 22.0], "T2": [18.0], "T3": []}
    mitjanes = {}
    for identificador, llista in dades.items():
        mitjanes[identificador] = mitjana(llista)
    print(mitjanes)



    print(informe_sensor("T1", [20.0, 22.0]))  
    print(informe_sensor("T2", [18.0]))
    print(informe_sensor("T3", [])) 