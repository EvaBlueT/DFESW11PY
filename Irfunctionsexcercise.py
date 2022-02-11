# Mathematical Calculations# 
# 
# def squared(x, y):
#     result = x**2 + y**2
#     return result

# x1 = float(input("Enter number1: "))
# y2 = float(input("Enter number2: "))

# print(squared(x1, y2))

# Population Dentisity task

# def population_density(var1, var2):
#     result = round(var2/var1)
#     return result

# var1 = float(input("Enter number of population: "))
# var2 = float(input("Enter land area: "))

# print("Population Detisity is: ", + population_density(var1, var2))



# def readable_timedelta(x):
#     weeks = x//7
#     days = x%7
#     return weeks, days

# x = int(input("Enter number of days: "))
# print(readable_timedelta(x))

cities = ['new york', 'mountain view', 'los angeles']
capitalised_cities = []

for city in cities:
    capitalised_cities.append(city.title())

print(capitalised_cities)

