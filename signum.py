bekert_szam = int(input("Adj meg egy számot!"))

if bekert_szam > 2022:
    print("nem jó a megadott év")
elif bekert_szam < 2012:
    print(f"ebben az évebn születtél: {bekert_szam}")
else:
    print("ebben az évtizedben született")
print("End")


