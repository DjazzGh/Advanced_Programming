
Stringinput = input("Please type in a string: ")
vowels = ['a', 'e', 'o']

for voyelle in vowels:
        if voyelle in Stringinput:
            print(f"{voyelle} found")
        else:
            print(f"{voyelle} not found")


