def get_list_statistics(user_list):
    if not user_list:
        return "List is empty. Cannot calculate statistics."

    mean = sum(user_list) / len(user_list)
    sorted_list = sorted(user_list)
    n = len(sorted_list)
    median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2 if n % 2 == 0 else sorted_list[n//2]

    return f"Mean: {mean}, Median: {median}"

def save_list_to_file(user_list, filename):
    with open(filename, 'w') as file:
        file.write("\n".join(map(str, user_list)))
    print(f"List saved to {filename}")

List = []
filename = "List.txt"

while True:
    try:
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        List.append(number)
        print(f"Current List: {List}")
        print(f"Sorted List (Ascending): {sorted(List)}")
        print(f"Sorted List (Descending): {sorted(List, reverse=True)}")
        print(get_list_statistics(List))
    except ValueError:
        print("Invalid input. Enter an integer.")

save_list_to_file(List, filename)
