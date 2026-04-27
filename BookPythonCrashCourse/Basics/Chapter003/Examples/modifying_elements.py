motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
print()

motorcycles[0] = "ducati"
print(motorcycles)
print()

motorcycles.append("triumph")
print(motorcycles)
print()

motorcycles.insert(0, "royal enfield")
print(motorcycles)
print()

motorcycles.remove("triumph")
del motorcycles[0]
print(motorcycles)
print()

poppedMotorcycle = motorcycles.pop()
print(poppedMotorcycle)
print(motorcycles)
print()

motorcycles.pop(0)
print(motorcycles)
