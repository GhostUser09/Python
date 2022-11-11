import numpy as np

argname = np.array([])
argnachname = np.array([])
argort = np.array([])
ausgabe = "Nein"
ausgabe2 = "Nein"
ausgabe3 = "Nein"
address = int()
program = "Ja"

#def edit(var):
while program == "Ja":
    print("NumPY Version: ", np.__version__)
    print("Was möchtest du tun?")
    start = input("\nSpeichern\nExportieren\nLesen\nLöschen\nZurück\n")
    if start == "Speichern":
        ausgabe = "Ja"
        ausgabe2 = "Nein"
        ausgabe3 = "Nein"

    if start == "Löschen":
        ausgabe = "Nein"
        ausgabe2 = "Nein"
        ausgabe3 = "Ja"

    if start == "Exportieren":
        export()

    if start == "Lesen":
        ausgabe = "Nein"
        ausgabe2 = "Ja"
        ausgabe3 = "Nein"

    if start == "Zurück":
        program = "Nein"
        ausgabe = "Nein"
        ausgabe2 = "Nein"
        ausgabe3 = "Nein"
        print("\nAuf wieder sehen!")

    while ausgabe == "Ja":
        name = input("Gib deinen Namen ein!\n")
        np.insert(name)
        nachname = input("Gib deinen Nachnamen ein!\n")
        np.insert(nachname)
        ort = input("Gib deinen Wohnort ein!\n")
        np.insert(ort)
        ausgabe = input("Möchtest du eine weitere Adresse hinzufügen?\n")

    while ausgabe2 == "Ja":
        ausgabe2 = input("Möchtest du eine Adresse ausgeben?\n")
        if ausgabe2 == "Ja":
            address = int(input("Welche Adresse möchtest du ausgeben\n"))

            print("\nVorname: ", argname[address])
            print("Nachname: ", argnachname[address])
            print("Ort: ", argort[address], "\n")

    while ausgabe3 == "Ja":
        delete = int(input("Welchen Eintrag willst du löschen?\n"))
        argname.pop(delete)
        argnachname.pop(delete)
        argort.pop(delete)
        ausgabe3 = input("Möchtest du einen weiteren Eintrag löschen")

    def export():
        format = input("Welches Format möchtest du benutzen?\nTXT oder CSV?")
        if format == "CSV":
            np.savetxt('PythonAdressen.csv', argname, argnachname, argort, delimiter=',')

        if format == "TXT":
            np.savetxt('PythonAdressen.txt', argname, argnachname, argort, delimiter=',')