cmimi_njesi = float(input("Cmimi njësi (Lek): "))
sasia = int(input("Sasia (copë): "))

if sasia < 0:
    print("Sasia e pavlefshme")
else:
    karte = input("Ke kartë studenti? (po/jo): ").lower().strip()
    nenshum = cmimi_njesi * sasia
    zbritje = 0
    if karte in ["po", "yes", "y"]:
        zbritje = nenshum * 0.10
    totali = nenshum - zbritje

    print("------------------------------")
    print("Nën-total:", format(nenshum, '.2f'), "Lek")
    print("Zbritja:", format(zbritje, '.2f'), "Lek")
    print("Totali:", format(round(totali, 2), '.2f'), "Lek")
tvsh = (nenshum - zbritje) * 0.15
totali += tvsh
print("TVSH (15%):", format(tvsh, '.2f'), "Lek")
