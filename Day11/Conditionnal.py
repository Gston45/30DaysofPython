#Exercices: Level 1
#1
'''def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(num1 = 1, num2=3))

#2
import math
def area_of_circle (r):
    area = math.pi * r * r
    return area
print(area_of_circle(4.5))

#3
def add_list_nums(*args):
    total = 0
    for num in args:
        if type(num) is int or type(num) is float:
            total += num
        else:
            print(f"{num} n'est pas un nombre")
    return total

print(add_list_nums(2, 12, "a", 34))
#4

def convert_celsius_to_fahrenheit (Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
print(convert_celsius_to_fahrenheit(50))

#5
def check_season(month):
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
print(check_season('january'))

#6
import math
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 8, 3, 6))

#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = -b + math.sqrt(discriminant) / 2*a
        x2 = -b - math.sqrt(discriminant) / 2*a
        return f"les solutions sont x1 = {x1} et x2 = {x2} "
    elif discriminant == 0:
        x = b / 2*a
        return f"on a une unique solution x = {x}"
    else:
        return "n'as pas de solution reelle"
print(solve_quadratic_eqn(2, 3, 6))

#8
def print_list(list):
    for item in list:
        print(item)
print_list(['ama', 'gregoire', 'kodjo'])


#9
def reverse_list(array):

    lst = []
    for i in range(len(array)-1 , -1, -1):
        #for i in range (n, m, pas)
        #range is use to generate index
        lst = lst + [array[i]]
    return lst
print(reverse_list(array = [1, 2, 3, 4, 5]))
'''
#10
def capitalize_list_items(items):
    liste = []
    for item in items:
       # item.capitalize()
        liste = liste + [item.capitalize()]
    return liste
print(capitalize_list_items(items=["Sirup", "Mango", "ira", "12"]))

#11




'''
#Exercices: Level 2
#1
def evens_and_odds(n):
    even = 0
    odds = 0
    for i in range (n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    print(f"The number of odds are{odds}")
    print(f"The number of even are {even}")

print(evens_and_odds(100))

#2

#3

#4


#Exercices: Level 3
'''