
prix = float(input("Please type in a price: "))

dinars = int(prix)
centimes = int(round((prix - dinars) * 100))

print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
