
numbers = [1, 2, 3, 4, 5]

def afficher_list():
    print("Updated List:", numbers)


while True:

        print("\nInitial List:", numbers)
        print("\nMenu:")
        print("1. Append")
        print("2. Insert")
        print("3. Pop ")
        print("4. Remove ")
        print("5. Quit")
        
        try:
            choice = int(input("Choose an option: "))

            if choice == 1:  
                value = int(input("Enter value to append: "))
                numbers.append(value)
                afficher_list()
            
            elif choice == 2:  
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index to insert at: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    afficher_list()
                else:
                    print("Error: Index out of range.")

            elif choice == 3:  
                if numbers:
                    index = int(input("Enter index to pop: "))
                    if 0 <= index < len(numbers):
                        numbers.pop(index)
                        afficher_list()
                    else:
                        print("Error: Index out of range.")
                else:
                    print("Error: List is empty.")

            elif choice == 4: 
                value = int(input("Enter value to remove: "))
                try:
                    numbers.remove(value)
                    afficher_list()
                except ValueError:
                    print(f"Error: {value} not found in the list.")
            
            elif choice == 5:  
                print("Exiting the program.")
                break
            
            else:
                print("Invalid option, please choose between 1 and 5.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


