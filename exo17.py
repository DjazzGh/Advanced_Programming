
numbers = []
shoe_sizes = []


for i in range(1, 6):
    numbers.append(i)


for size in range(8, 13):
    shoe_sizes.append(size)


print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)


numbers.append(3)  

print("Updated Numbers List with Duplicates:", numbers)

combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)
