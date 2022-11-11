l = float(input("Geben Sie die Länge an!\n"))
b = float(input("Geben Sie die Breite an!\n"))
h = float(input("Geben Sie die Höhe an!\n"))
t = float(input("Geben Sie die Torgröße an!\n"))
qmp = float(input("Geben Sie den Quadratmeterpreis an!\n"))
e = (l+l-t)+(b*2)*h
g = round(e, 3)
gp = g*qmp
gpg = round(gp, 2)

print("Es werden", g, "Meter Zaun benötigt")
print("Der Gesamtpreis beträgt", gpg, "Euro")


