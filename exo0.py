
num_personnes = int(input("How many people need a ride? "))
taxi_capacité = int(input("How many people fit in one taxi? "))


num_taxis = num_personnes // taxi_capacité
if num_personnes % taxi_capacité != 0:
    num_taxis += 1

print(f"Number of taxis needed: {num_taxis}")
