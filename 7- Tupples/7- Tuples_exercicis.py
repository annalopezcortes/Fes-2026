# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
tupla_ciutats = ("Barcelona", "Berlin", "Madrit", "Paris", "Tokio")
print(f"Segona ciutat: ", tupla_ciutats[1])
print(f"Penúltima ciutat: ", tupla_ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
tupla_enters = (3,4,2,6,7,5,3,3,1)
print(f"Apareix {tupla_enters.count(3)} vegades el numero 3")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tupla.sort()

numeros_desordenats = (3,5,1,2,7,8,9,2)
numeros = ordenar_tupla(numeros_desordenats)
print ("Tupla ordenada: ", numeros)