empty_string=False
while empty_string==False:
    userString = input("Type in a string: ")
    
    if userString == "":
        empty_string=True
    
    print(userString)
    print("-" * len(userString))
