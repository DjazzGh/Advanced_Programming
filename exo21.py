def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def get_list_statistics(lst):

    if not lst:
        return "List is empty. Cannot calculate statistics."

    return {
        "length": len(lst),
        "mean": mean(lst),
        "median": median(lst),
        "range": max(lst) - min(lst),
        "standard_deviation": standard_deviation(lst)
    }


List_utilisateur = input("Enter a list of numbers separated by spaces: ")
try:
        user_list = list(map(float, List_utilisateur.split()))
        stats = get_list_statistics(user_list)
        if isinstance(stats, str):
            print(stats)
        else:
            for key, value in stats.items():
                print(f"{key.capitalize()}: {value}")
except ValueError:
        print("Invalid input")

