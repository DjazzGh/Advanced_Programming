
city_population = {}

while True:
    city = input("Enter the name of a city: ").strip()
    if city.lower() == 'stop':
        break
    city_population[city] = len(city) * 1000000


cities_trié = sorted(city_population.items(), key=lambda x: x[1], reverse=True)


print("\nCities and their populations :")
for city, population in cities_trié:
    print(f"The city {city} has {len(city)} letters so its population is {population} citizens")
