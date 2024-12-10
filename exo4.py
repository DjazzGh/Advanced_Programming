
FirstAge = int(input("Please type in the age of the first person: "))
SecondAge = int(input("Please type in the age of the second person: "))


if FirstAge > SecondAge:
    print("The older age is:", FirstAge)
elif SecondAge > FirstAge:
    print("The older age is:", SecondAge)
else:
    print("Both people are the same age!")
