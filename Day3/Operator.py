#1 Declare age
age = 20
age = int(age)

#2 Declare Height

height = 1.81
height = float(height)

#3 complex number

num = 4 + 9j

#4 Script

b = input("Enter base :")

h = input("Enter height :")

b = int(b)
h = int(h)

area = 0.5 * b * h

print("The area of the triangle is :", area)

#5 Script 

a = input("Enter side a :")

b = input("Enter side b :")

c = input("Enter side c :")

a = int(a)
b = int(b)
c = int(c)

perimeter = a + b + c

print("The perimeter of the triangle is :", perimeter)


#6 length and width of a rectangle using prompt

lenght = input("Enter lenght :")

width = input("Enter width :")

lenght = int(lenght)    
width = int(width)      

perimeter = 2 * (lenght + width)

area = lenght * width

print("erea is : ", area)

print("perimeter is :", perimeter)

#7 radius of a circle using prompt

r = input("Enter radius :")

r = int(r)
pi = 3.14

area = pi * r * r

c = 2 * pi * r

print("The area is :", area, ",", "Te circumference is :", c)

#8 The slope 

#y = mx + 2  ==>  slope = m

m = 2

print("slope m = ",m)
#y = 2x - 2   ==> m = 2

#y-intercept
#when x = 0

x = 0
y = (2 * x) - 2
print("y-intercept (0, {})".format(y))

#x-intercept
#when y = o

y = 0
x = (y + 2) / 2
print("x-intercept ({}, 0)".format(x))


#9 The slope and Euclidean distance

x1 = 2
x2 = 6
y1 = 2
y2 = 10

m = y2 - y1 /x2 -x1
import math

E =math.sqrt (m) 

print("Euclidian distance =", E)


#10 comparate the slopes

print(m > E)


#11 y value

x = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

y = x + 2
print(y)


#12 comparison
python = "python"
dragon = "dragon"

print(len(python) == len(dragon) )


#13 checking

on = "on"
print(on in python and on in dragon)


#14 checking

test = str("i hope this course is not full jargon")
jargon = str("jargon")
print(jargon in test)


#15
print(on not in dragon and python)

#16
w = len(python)
print("lenght is", w)

w = float(w)
print(w)

#17 
x = int(input("Enter a number:"))

if x % 2 == 0 :
    print("number are divisible by 2")
else:
    print("number are not divisible by 2")

#18
x = 7 // 3
print(x == 2.7)


#19
print(type('10') == type(10))

#20
print(int(9.8) == 10)

#21
#######script
hours = input("Enter hours:")
rate = input("Enter rate per hour:")
earn = input("Your weekly earning is:")

hours = int(hours)
rate = int(rate)

#####Pay of the person

pay = hours * rate

print("Pay of the person is:", pay)

#22
years = input("Enter number of years you have lived:")

years = int(years)

####number of second

seconds = 365 * 24 * 60 * 60

lived = years * seconds

print("You have lived for", lived,"seconds")

#23
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
