'''#Exercices: Level 1
#1
age = input("Enter your age:")
age = int(age)
print(age)

if age >= 18:
    print("You are old enough to drive")
else:
    missing_amount = 18 - age
    missing_amount = int(missing_amount)
    print("You need ",missing_amount," more years to learn to drive")

#2
my_age = 19
your_age = input("Enter your age:")
your_age = int(your_age)
difference_of_age = your_age - my_age

if my_age > your_age:
    print("i'm older than you")

elif my_age == your_age:
    print("we are the same age")
else:
    print("you're ", difference_of_age, "yeras older then me")

#3
a = input("Enter number One:")
b = input("Enter number two:")
a = int(a)
b = int(b)

if a > b:
    print(a, "is greater than ", b)
elif a < b :
    print(a, "is smaller than ", b)
else:
    print(a, "is equal to ", b)


#Exercises: Level 2
#1
scores = {
    "A": "80 - 100",
    "B" : "70 - 89",
    "C" : "60 - 69",
    "D" : "50 - 59",
    "F" : "0 - 49"
 }

#2
Autumn = ('September', 'October', 'November')
Winter = ('December', 'January', 'February')
Spring = ('March', 'April', 'May')
Summer = ('JUne', 'July', 'August')

mounth = input("Enter the mounth:")
mounth = str(mounth)

if mounth in Autumn:
    print("The season is Autumn.")

elif mounth in Winter:
    print("The season is Winter.")
elif mounth in Spring:
    print("The season is Spring")
else:
    print("The season is Summer")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
new_fruit = input("Add a new fruits: ")
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(fruits)
'''
#Exercices: Level 3
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB',
'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

#1
if 'skills' in person:
    skills = person['skills']
    middle = len('skills') // 2
    print('the middle skill in the skills list is :', skills[middle])

#2
if 'skills' in person:
    skills = person['skills']
    pyhton_skills = 'Python' in skills
    print(pyhton_skills)

#3
if 'skills' in person:
    skills = person['skills']

    if 'JavaScript' in skills and 'React' in skills:
        print('He\is a front end developer')
    elif 'Python' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('he\'s a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He\'s a fullstack developer')
    else:
        print('unknown title')

#4
if 'is_marred' in person and 'country' in person:
    is_marred = person['is_marred']
    country = person['country']
    if is_marred is True and country is 'Finland':
        print('Asabeneh Yetayeh lives in Finland. He is married.')
