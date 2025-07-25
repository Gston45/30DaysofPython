#Jour2: 30 Days of Python Programming

#Exercice Niveau 1

Prenom = "Gedeon"
Nom_de_famille = "JULIEN"
nom_complet = "JULIEN Gedeon"
Pays = "Togo"
Annee = 2025
Is_Married = 2015
Is_true = "yes"
Is_light_on = "yes"
multiple = 1,2,3,4,5,6,7,8,9,0



#exercice Niveau 2

#type des donne de tout les variables

print(type(Prenom))
print(type(Nom_de_famille))
print(type(nom_complet))
print(type(Pays))
print(type(Annee))
print(type(Is_Married))
print(type(Is_true))
print(type(Is_light_on))
print(type(multiple))

#fonction integre len() de prenom

print(len(Prenom))

#comparaison de la longueur du prenom et du nom

print(len(Prenom) == len(Nom_de_famille))

# Declaration
num_one = 4
num_two = 5

#Add num_one et num_two

total = num_one + num_two

print(total)

#Substraction

diff = num_one - num_two
print(diff)

#Multiply

product = num_one * num_two

print(product)

#Divide

division = num_one / num_two

print(division)

#modulus

remainder = num_two % num_one

print(remainder)

#exp

exp = num_one ** num_two
print(exp)

#floor division

floor_division = num_one // num_two

#12.i Calcul the area
import math

rayon = 30

area_of_circle = float(math.pi) * (rayon ** 2)

print(area_of_circle)

#12.ii Calcul the circumference

diametre = rayon * 2

circum_of_circle = float(math.pi) * diametre

print(circum_of_circle)

#12.iii calul the area using user input

radius = input("radius : ")
radius = int(radius)

area = float(math.pi) * (radius ** 2)

print(area)

#Input function

#first name

first_name = input("First name : ")
first_name = str(first_name)

print(first_name)

#last name

last_name = input("last name : ")
last_name = str(last_name)

print(last_name)

#country

country = input("country : ")
country = str(country)

print(country)

#age

age = input("age : ")
age = int(age)

print(age)

