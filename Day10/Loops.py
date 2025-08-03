#Exercices: Level 1
#1

# while method
i = 0
a = 0
while a <= 10:
    print(a)
    a = a + 1

# for method
a = range(11)
for i in a:
    print(i)

#2
i = 10
while i > 0:
    print(i)
    i = i - 1

a = range(10, -1, -1)
for i in a:
    print(i)
  
#3
for i in range(1, 8):
    print("#" * i)



#4
a = 1
while a <= 7:
    print('#' * a)
    a = a + 1
    

a = range(8)
for i in a:
    for j in a:
        print('#',end=" ")
    print()



#5
a = 1
r = a * a
while a <= 10:
    print(a,'*', a ,"=", r)
    a = a + 1
    r = a * a

#6
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list:
    print(i)
    

#7
a = range(0, 101)
for i in a:
    print(i)
    a = i + 1
    

#Exercices: Level 2

somme = 0
for i in range(0, 101):
    somme = somme + i
print(somme)


somme = 0
print("avant la boucle")
print(somme)

for i in range(0, 11):
    print("dans la boucle")
    print(f"somme = {somme} + {i}")
    somme = somme + i

print("après la boucle")
print(somme)

#2
somme_paire = 0
somme_impaire = 0
for i in range(0, 101):
    if i % 2 == 0:
        somme_paire += i
    else:
        somme_impaire += i
print(f"The sum of all evens is {somme_paire}. And the sum of all odds is {somme_impaire}")
