###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
num = 10
while (num>1):
    print(num)
    num-=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
numero = 1
suma = 0
while(numero<21):
    if (numero%2==0):
        suma += numero
    mumero+=1

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número.
# Per exemple, el factorial de 5: 5! = 5 x 4 x 3 x 2 x 1 = 120.
factorial = 5
multiplicació = factorial
while (factorial!=0):
    factorial-=1
    multiplicació *=factorial
print("El factorial és:", multiplicació)

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contraseña = input("Afegeix una contraseña de 8 caracters: ")
while (len(contraseña)<8):
    print("Contrasenya invalida")
    contraseña = input("Afegeix una contraseña vàlida: ")

print("Contrasenya correcta")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix un numero: "))
taula = 1
while (taula<=10):
    resultat = taula*numero
    print(f"{numero} * {taula} = {resultat})
    taula+=1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
N = int(input("Introdueix un número enter positiu N: "))
num = 2

while num <= N:
    i = 2
    es_primer = True
    while i < num:
        if num % i == 0:
            es_primer = False
            break
        i += 1
    if es_primer:
        print(num)
    num += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
enter = 1
suma = 0
while enter != 0:
    enter = int(input("Introdueix un enter (0 per sortir del bucle): "))
    suma +=enter
    
print("Suma total: ", suma)

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
contador = 0
positiu = int(input("Introdueix un número enter positiu: "))
while (positiu>0):
    contador +=1
    positiu = positiu//10
    
print(f"{positiu} té {contador} xifres")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
termes = int(input("Quants termes de Fibonacci vols veure? "))
a, b = 0, 1
comptador = 0

while comptador < termes:
    print(a)
    següent = a + b
    a = b
    b = següent
    comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
numero = 30
proba = int(input("Prova d'endevinar el numero secret: "))
while (numero != proba):
   if(numero>proba):
        print("És més gran")
    elif (numero<proba):
        print("És més petit")
    else:
        print("Has acertat!")
    proba = int(input("Torna a probar: "))

print(f"El numero secret era {numero}!")
