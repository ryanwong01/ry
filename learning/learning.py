# Madlibs game
# word game where you create a story
# by filling in blanks with random words
from operator import truediv

from PyInstaller.utils.hooks.conda import collect_dynamic_libs

'''adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing ")
adjective3 = input("Enter an adjctive (description): ")

print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")


friends = 0

# friends = friends + 1
friends += 1 # augmented assignment operators
friends = friends - 2
friends -= 2
friends = friends * 3
friends *= 3
friends = friends / 2
friends /= 2
friends = friends ** 2
friends **= 2
remainder = friends % 2
print(friends)

import math

x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x)
x = 3.14
y = 4
z = 5

result = round(x)
result = abs(y)
result = pow(4 , 3)
result = max(x, y, z)
result = min(x ,y ,z)

print(result)

import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius , 2)

print(f"The area of the circle is: {round(area, 2)} cm^2")


#Python weight converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)}{unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)}{unit}")
else:
    print(f"{unit} is an invalid unit of measurement")

unit = input("Is the temperature is Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} °F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is: {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement")

#logical operators = evaluate multiple conditions ( or, and, not)
     #               or = at least one condition must be true
     #               and = both conditions must be true
     #               not = invrets the condition ( not False, not True)

  #  temp = 25
  #  is_raining = False

  #  if temp > 35 or temp < 0 or is_raining:
  #      print("The outdoor event is cancelled")
  #  else:
  #      print("The outdoor event is still scheduled")

#temp = 25
#is_sunny =  True

#if temp >= 28 and is_sunny:
 #   print("It is HOT outside)
 #   print("It is SUNNY")

#elif temp <= 0 and is_sunny:
 #   print("It is cold outside")
 #   print("It is SUNNY")

#elif 28 > temp > 0 and is_sunny:
  #  print("it is warm outside")
  #  print("It is SUNNY")

#elif temp >= 28 and not is_sunny:
  #  print("It is HOT outside")
 #   print("It is CLOUDY")

#elif(temp <= 0 and not is_sunny):
  #  print("it is COLD outside")
  #  print("it is CLOUDY")

#Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                       Print or assign one of two values based on a condition
#                       X if condition else Y

num = 6
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

# print("positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD")
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "adult" if agge >= 18 else "child"
# weather = "Hot" if temperature > 20 else "Cold"
# print(weather)
#print(status)
# print(result)
#access_level + "full Access" if user_role == "admin" else "limited access"
'''
'''''
#name = input("Enter your full name: " )
phone_number = input("ENter your phone number: ")
#result = len(name)
# result = name . find ("o")
# result = name.rfind("q")
# name - name. capatalzie ()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
#result = phone_number.count("-")
phone_number = phone_number.replace("-", " ")

print(phone_number)

'''''
# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
credit_number[5:]










