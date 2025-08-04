#Exercices
#1 (Filter only negative and zero in the list)
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
number = [i for i in numbers if i <= 0]
print(number)

#2 (Flatten the list)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Flatened_lists = [number for row in list_of_lists for number in row]
print(Flatened_lists)

#3 (create list of tuples)
result = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(result)

#4 (Flatten list to a new list)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
Flattened_country = [
    [country,country[:3].upper(), city]
    for sublist in countries
    for(country, city) in sublist
]
print(Flattened_country)

#5 (change list to a liste to dictionnaries)
#import countries to #4
country_dict = [
    {'country': country, 'city': city}
    for sublist in countries
    for(country, city) in sublist
]
print(country_dict)

#6 (list of concatenated strings)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_strings = [
    f'{first} {last}' for sublist in names for (first, last) in sublist
]
print(concatenated_strings)

#7 (lambda function)
slope = lambda x1, y1, x2, y2 :y2 - y1 // x2 - x1
print(slope(1, 2, 3, 4))