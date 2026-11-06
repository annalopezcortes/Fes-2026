# Gestor i analitzador d'incidències de telecomunicacions

def mostrar_menu():
    print("\n--- GESTOR D'INCIDÈNCIES DE TELECOMUNICACIONS ---")
    print("1. Registrar nova incidència")
    print("2. Llistar totes les incidències")
    print("3. Marcar incidència com a resolta")
    print("4. Analitzar estat de la xarxa")
    print("5. Sortir")

def registrar_incidencia(incidencies):
    id_inc = f"INC-{len(incidencies) + 1:03d}"
    print(f"\n--> Registrant nova incidència amb ID: {id_inc}")
    
    tipus = input("Tipus de problema (ex: Fibra, Router Wi-Fi, Centralita): ")
    prioritat = input("Prioritat (Baixa, Mitjana, Alta, Crítica): ")
    descripcio = input("Descripció breu del problema: ")
    
    nova = {
        "id": id_inc,
        "tipus": tipus,
        "prioritat": prioritat,
        "estat": "Pendent",
        "descripcio": descripcio
    }
    
    incidencies.append(nova)
    print("¡Incidència registrada correctament!")

def llistar_incidencies(incidencies):
    if not incidencies:
        print("\nNo hi ha incidències registrades.")
        return
        
    print("\n--- LLISTA D'INCIDÈNCIES ---")
    for inc in incidencies:
        print(f"[{inc['id']}] {inc['tipus']} | Prioritat: {inc['prioritat']} | Estat: {inc['estat']}")
        print(f"    Descripció: {inc['descripcio']}")
        print("-" * 40)

def resoldre_incidencia(incidencies):
    llistar_incidencies(incidencies)
    if not incidencies:
        return
        
    id_buscar = input("\nIntrodueix l'ID de la incidència a resoldre (ex: INC-001): ").strip()
    
    trobada = False
    for inc in incidencies:
        if inc['id'].lower() == id_buscar.lower():
            inc['estat'] = "Resolt"
            print(f"¡La incidència {inc['id']} ha estat marcada com a Resolta!")
            trobada = True
            break
            
    if not trobada:
        print("No s'ha trobat cap incidència amb aquest ID.")

def analitzar_incidencies(incidencies):
    if not incidencies:
        print("\nNo hi ha dades per analitzar.")
        return
        
    total = len(incidencies)
    pendents = sum(1 for inc in incidencies if inc['estat'] == "Pendent")
    resoltes = sum(1 for inc in incidencies if inc['estat'] == "Resolt")
    critiques = sum(1 for inc in incidencies if inc['prioritat'].lower() == "crítica" and inc['estat'] == "Pendent")
    
    print("\n--- ANÀLISI DE LA XARXA ---")
    print(f"Total d'incidències: {total}")
    print(f"Incidències pendents: {pendents}")
    print(f"Incidències resoltes: {resoltes}")
    print(f"Incidències crítiques pendents: {critiques}")

def main():
    incidencies = []
    while True:
        mostrar_menu()
        opcio = input("\nTria una opció (1-5): ")
        
        if opcio == "1":
            registrar_incidencia(incidencies)
        elif opcio == "2":
            llistar_incidencies(incidencies)
        elif opcio == "3":
            resoldre_incidencia(incidencies)
        elif opcio == "4":
            analitzar_incidencies(incidencies)
        elif opcio == "5":
            print("\nSortint del programa. Fins aviat!")
            break
        else:
            print("\nOpció no vàlida. Tria un número entre l'1 i el 5.")

if __name__ == "__main__":
    main()