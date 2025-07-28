#Exercices; Level 1
#1
empty_tuple = tuple()
print(empty_tuple)

#2
name_of_sisters_and_brothers = ('lea', 'yanis', 'VIMPKE', 'ama', 'gregoire')
print(name_of_sisters_and_brothers)

#3
Family_members= tuple(name_of_sisters_and_brothers)
print(Family_members)

#4
number = len(Family_members)
print(number)

#5
Family_members = list(Family_members)
print(Family_members)
Parents = 'Malik', 'Anita'
Family_members.extend(Parents)
print(Family_members)


#Exercices: Level 2
#1
print(len(Family_members))
del Family_members[5:7]
print(Family_members)

#2
fruit_name = ('orange', 'banana', 'mango', 'apple')
fruits = tuple(fruit_name)
vegetables_name = ('carrot', 'cabbage', 'aggplant', 'brocolli')
vegetables = tuple(vegetables_name)
animal_name = ('dog', 'cat', 'snake', 'bird')
animal = tuple(animal_name)
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#3
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

#4
x = len(food_stuff_tp) // 2
print(x)
print(food_stuff_tp[x])

#5
print(food_stuff_tp[0:3])
print(food_stuff_tp[-3:])

#6
del food_stuff_tp

#7
nordic_countries_name= ('Denmark', 'Finland','Iceland', 'Norway','Sweden')
nordic_countries = tuple(nordic_countries_name)
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)