#Exercices: Day8
#1
dog = ()
print(dog)

#2
dog ={
    'name',
    'color',
    'breed',
    'leg',
    'age'
}
print(dog)

#3
student_dict = {
    'first_name' : 'Vimpkpe',
    'last_name' : 'kodjo',
    'gender' : 'Male',
    'age' : '18',
    'marital status' : 'married',
    'skills' : ['python', 'html', 'js'],
    'country' : 'Senegal',
    'city' : 'Dakar',
    'adress' : 'street 4th arrondissement'

}
print(student_dict)

#4
print(len(student_dict))

#5
skills_value = student_dict['skills']
print(skills_value)

data_type = type(skills_value)
print(data_type)

#6
skills_value = list(skills_value)
skills_value.append('managment')
skills_value.append('Cybersecurity')
print(skills_value)

#7
skills_value = list(student_dict.keys())
print("num7\n")
print(skills_value)


#8
values = list(student_dict.values())
print(values)

#9
tuples = student_dict.items()
print(tuples)

#10
student_dict.pop('first_name')
print(student_dict)

#11
del tuples
'''
print(tuples)   error because tuples has been deleted 

'''