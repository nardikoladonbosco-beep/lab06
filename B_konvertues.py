# Leximi i kilometrave
km = float(input("Kilometra: "))
m = km * 1000

# Leximi i ditëve
ditet = int(input("Ditë qëndrimi: "))

# Output
print("Do të ecësh", m, "metra në total dhe do të rrish", ditet, "ditë.")
print("Tipet:", type(m), "dhe", type(ditet))
njesia = input("Njësia (km/mi): ").lower().strip()
if njesia == "mi":
    km = float(input("Milje: ")) * 1.609
else:
    km = float(input("Kilometra: "))
m = km * 1000
ditet = int(input("Ditë qëndrimi: "))
print("Do të ecësh", m, "metra në total dhe do të rrish", ditet, "ditë.")
print("Tipet:", type(m), "dhe", type(ditet))
