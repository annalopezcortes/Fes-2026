###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom = input("Nom del tècnic: ")
xarxa = input("Nom xarxa: ")
print(f"Nom del tècnic: {nom}\nXarxa que esta instalant: {xarxa}\n")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Longitud cable fibra òptica (Km): "))
velocitat_transmissió = float(input("Velocitat de transmisió (Gbps): "))

temps_transmissió_GB =8/velocitat_transmissió
print(f"Per transmetre 1 GM calen {temps_transmissió_GB}\n")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = float(input("Nombre d'hores: "))
preu_hora = float(input("Preu pero hora d'instal·lació: "))
preu_material = float(input("Preu del material: "))
cost_total = hores*preu_hora + preu_material
print(f"El cost total d'instal·lació és de {cost_total} euros")
