#Exercices : Day7
#set

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercices : Level 1
#1
print(len(it_companies))

#2
it_companies.add('Twitter')
print(it_companies)

#3
multiple_it_companies = ('Alibaba', 'Togocom', 'Yahoo')

it_companies.update(multiple_it_companies)
print(it_companies)

#4
it_companies.pop()
print(it_companies)

#5
'''
remove  method will raise error, while discard method doesn't raise any error
'''

#Exercices :Level 2
#1
AB = A.union(B)
print(AB)

#2
inter = A.intersection(B)
print(inter)

#3
subset = A.issubset(B)
print(subset)

#4
disjoint = A.isdisjoint(B)
print(disjoint)

#5
#A with B 
print(AB)

#B with A
BA = B.union(A)
print(BA)

#6
sym = A.symmetric_difference(B)
print(sym)

#7
del A
del B
'''
print(A)
print(B)  ##error answers because A and B has removed
'''


#Exercices : Level 3
#1
age_set = set(age)
print(len(age_set) == len(age))

#2
"""
String:

    Mutability: Immutable. Once created, a string's characters cannot be changed.
    Order: Ordered. Characters are stored in a defined sequence and can be accessed by index.
    Duplicates: Allows duplicate characters. 

List:

    Mutability: Mutable. Elements can be added, removed, or modified after creation.
    Order: Ordered. Elements are stored in a defined sequence and can be accessed by index.
    Duplicates: Allows duplicate elements. 

Tuple:

    Mutability: Immutable. Once created, a tuple's elements cannot be changed.
    Order: Ordered. Elements are stored in a defined sequence and can be accessed by index.
    Duplicates: Allows duplicate elements. 

Set:

    Mutability: Mutable (elements can be added or removed), but individual elements themselves must be immutable (e.g., numbers, strings, or tuples).
    Order: Unordered. Elements are not stored in a specific sequence and cannot be accessed by index.
    Duplicates: Does not allow duplicate elements; only unique elements are stored.


"""

#3
sentence = "I am a teacher and I love to inspire and teach people"

sentence_1 = set("I am a teacher")
sentence_2 = ("and I love to inspire and teach people")

unique_word = sentence_1.intersection(sentence_2)
print(unique_word)
