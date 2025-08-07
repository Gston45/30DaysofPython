#Exercices

from datetime import datetime    #datetime module

#1 (The current day)
now = datetime.now()
print(now)

#2 (Formatage)
now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now)

#3 (Change string to time)
today = "5 December, 2019"
string_to_time =datetime.strptime(today, "%d %B, %Y")
print(string_to_time)

#4 (Difference between now and new year)

now = datetime(year = 2025, month= 8, day= 7)
new_year = datetime(year= 2026,month= 1, day=1)
difference = new_year - now
print(difference)

#5 (difference between 1 january 1970 and now)
diff = now.timestamp()
print(diff)

#6
'''
i can use the datetime module to publish newsletters mail to my community'''