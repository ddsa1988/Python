cars: list[str] = ["bmw", "audi", "toyota", 'subaru']
print(cars)

# The sort method changes the original list
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
print()

# The sorted function doesn't change the original list
cars = ["bmw", "audi", "toyota", 'subaru']
cars_sorted = sorted(cars)
cars_sorted_reverse = sorted(cars, reverse=True)
print(f"Original list: {", ".join(cars)}")
print(f"Sorted list: {", ".join(cars_sorted)}")
print(f"Sorted reverse list: {", ".join(cars_sorted_reverse)}")
print()

# The reverse function simply reverses the order of the list
cars = ["bmw", "audi", "toyota", 'subaru']
print(cars)
cars.reverse()
print(cars)
