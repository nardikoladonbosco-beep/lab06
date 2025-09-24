# Deklarime të paracaktuara
mosha = 17
cmimi = 149.99
emri = "Arta"
ka_karte = True

# Printimi i vlerave dhe tipeve
print(emri, type(emri))
print(mosha, type(mosha))
print(cmimi, type(cmimi))
print(ka_karte, type(ka_karte))

# Input dhe shndërrim
vlera1 = input("Shkruaj një numër të plotë: ")
print("Tipi fillestar:", type(vlera1))
vlera1_int = int(vlera1)
print("Pas shndërrimit:", type(vlera1_int))

vlera2 = input("Shkruaj një numër me presje: ")
print("Tipi fillestar:", type(vlera2))
vlera2_float = float(vlera2)
print("Pas shndërrimit:", type(vlera2_float))
