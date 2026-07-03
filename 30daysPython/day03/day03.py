#
# Day 3 - Perosnal Profile and BMI Calculator.
# - Topics Covered :
# - Variables
# - Data Types
# - Type Casting
# - Arithmetic Operators
# - f-String
# 
print("=" * 50)
print(" WELCOME TO THE PERSONAL PROFILE GENERATOR")
print("=" * 50)

# User Input
name = input("Enter your name : ")
age = int(input(" Enter your age : "))
height = float(input(" Enter your height(in cm): "))
weight = float(input(" Enter your weight (in kg): "))
city = input (" Enter your city : ")
language = input(" Enter your language : ")

# Calculations
height_m = height / 100
bmi = weight / (height_m ** 2)

birth_year = 2026 - age

# Output 

print("/n" + "=" * 50)
print("YOUR PROFILE")
print("=" * 50)

print(f"Name {name}")
print(f" Birth_Year{birth_year}")
print(f" Age{age}")
print(f" Favourite_Language{language}")
print(f" City {city}")
print(f" Height {height}")
print(f" Weight {weight}")
print(f" BMI{round (bmi , 2)}")

print("/n------DATA TYPES------")
print(type(name))
print(type(age))
print(type(height))
print(type(weight))
print(type(language))
print(type(bmi))
print(type(city))

print("/n------TYPE CONVERSIONS------")
age_string = str(age)
weight_integer = int(weight)
height_integer = int(height)


print(" Age as String : ",age_string)
print(" Weight as Integer : ", weight_integer)
print(" Height as Integer : ", height_integer)

print("/n------SUMMARY------")

print(f"Hello {name}! You are {age} Years old and I live in {city} .")
print(f"You enjoy learning {language}.")
print(f" Your calculated BMI is {round(bmi , 2)}.")

print("/n Thank you for using Personal Profile Generator.")


