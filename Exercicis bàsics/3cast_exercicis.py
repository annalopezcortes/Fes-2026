###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
print("Quants paquets ha rebut un encaminador?")
paquets_rebuts = int(input())
print(f"Total de paquets: {paquets_rebuts + 1200}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
print("Quina es la velocitat d'una conexió (Mbps)")
velocitat_Mbps = float(input())
velocitat_MBps = velocitat_Mbps / 8
print(f"La velocitat equivalent en MB/s és:{velocitat_MBps}")