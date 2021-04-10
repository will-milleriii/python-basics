cities = {"Barcelona", "Paris", "London", "New York"}

print(len(cities))
print(type(cities))
cities.add("Milan")

otherCities = set(("Miami", "Liverpool", "Munich"))

otherCities.update(cities)
print(otherCities)
print(type(otherCities))


for i in cities:
    print(i)