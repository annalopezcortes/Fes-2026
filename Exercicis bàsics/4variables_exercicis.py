###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
print("Dades d'un encaminador: ")
Nom_encaminador = str(input("Nom encaminador: "))
Ubicacio = str(input("Ubicació: "))
Nombre_ports = int(input("Nombre de ports: "))
Encés = str(input("Estat: "))
print(f"Nom encaminador: {Nom_encaminador}; Ubicació: {Ubicacio}; Nombre de ports: {Nombre_ports}; Estat: {Encés}")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
nombre_GB = float(input("Gigabaits inclosos: "))
consumits_GB = float(input("Gigabaits consumits: "))
print(f"Queden {nombre_GB - consumits_GB} disponibles encara.")
consumits_GB = float(input("Nou valor de Gigabaits consumits: "))
print(f"Ara queden {nombre_GB - consumits_GB}")