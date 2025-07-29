# Autor: Roman Janotík
# Projekt: Task Manager

# Seznam
ukoly = []

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if not nazev or not popis:
            print("Název i popis úkolu musí být vyplněny. Zkuste to prosím znovu.\n")
        else:
            ukoly.append({"nazev": nazev, "popis": popis})
            print(f"Úkol '{nazev}' byl přidán.\n")
            break

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou k dispozici.\n")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
        print()

def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný. Není co mazat.\n")
        return

    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu k odstranění: "))
        if 1 <= cislo <= len(ukoly):
            smazany = ukoly.pop(cislo - 1)
            print(f"Úkol '{smazany['nazev']}' byl odstraněn.\n")
        else:
            print("Neplatné číslo úkolu.\n")
    except ValueError:
        print("Zadejte platné číslo.\n")

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.\n")

# Spustenie
hlavni_menu()