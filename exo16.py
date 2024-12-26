
numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter index (-1 to quit): "))
             
        if index == -1:
            break
        
        if index < 0 or index >= len(numbers):
            print("Invalid index! out of range")
            continue

       
        nouvelle_valeur = input("Enter new value: ")
   
        try:
            nouvelle_valeur = int(nouvelle_valeur)
        except ValueError:
            print("Invalid value! not an integer")
            continue

       
        numbers[index] = nouvelle_valeur

        print(numbers)
    
    except ValueError:
        print("Invalid index!")
