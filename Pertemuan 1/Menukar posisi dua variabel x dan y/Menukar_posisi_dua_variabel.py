def pemindahan(x, y, z):
    z = x
    x = ""
    print("[Pemindahan Pertama]")
    print(f"Piring 1 = {x}")
    print(f"Piring 2 = {y}")
    print(f"Piring 3 = {z}")
    x = y
    y = ""
    print("")
    print("[Pemindahan Kedua]")
    print(f"Piring 1 = {x}")
    print(f"Piring 2 = {y}")
    print(f"Piring 3 = {z}")
    y = z
    z = "" 
    print("")
    print("[Pemindahan ketiga]")
    print(f"Piring 1 = {x}")
    print(f"Piring 2 = {y}")
    print(f"Piring 3 = {z}")

piring_1 = "Manggis"
piring_2 = "Pisang"
piring_3 = ""
print("[Sebelum diubah]")
print(f"Piring 1 = {piring_1}")
print(f"Piring 2 = {piring_2}")
print(f"Piring 3 = ")
print()
pemindahan(piring_1, piring_2, piring_3)