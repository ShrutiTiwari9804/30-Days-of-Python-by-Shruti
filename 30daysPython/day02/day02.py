# Day 2 - Variables and Data Types
# Project : Student Profile Generator 

# String 
name = "Shruti"

# Integer 
age = 21

# Float
height = 153.5

# Boolean
is_backend_aspirant = True

# List
skills = ["Python", "Git", "Github"]

# Tuples 
favorite_languages = ("Python", "SQL")

# Dictionary
social = {"Github": "github.com/shruti", "LinkedIn": "linkedin.com/in/shruti"}

# Set
hobbies = {"Codding", "Reading", "Workout"}

print("=" * 40)
print("STUDENT PROFILE")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height:{height}")
print(f"Backend Aspirant:{is_backend_aspirant}")
print(f"Skills: {skills}")
print(f"Favorite Languages:{favorite_languages}")
print(f"Social Links:{social}")
print(f"Hobbies:{hobbies}")

print("\n----DATA TYPES----")
print(type(name))
print(type(age))
print(type(height))
print(type(is_backend_aspirant))
print(type(skills))
print(type(favorite_languages))
print(type(social))
print(type(hobbies))

print("\n-----TYPE CONVERSION----")
age_string = str(age)
height_integer = int(height)
age_float = float(age)

print(age_string,
type(age_string))
print(height_integer,
type(height_integer))
print(age_float,
type(age_float))