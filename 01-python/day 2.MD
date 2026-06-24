Day 2: Python Basics
Goal

Learn the basic Python building blocks needed for AI Product Management, Data Science, and automation work.

Topics Covered
1. Variables

Variables store information.

name = "Fares"
city = "Dubai"
target_role = "AI Product Manager"
2. Data Types

Python values have different types.

name = "Fares"              # string
years_experience = 8        # integer
mba_gpa = 3.96              # float
is_learning_ai = True       # boolean

Main types learned:

str: text
int: whole number
float: decimal number
bool: true or false
3. Lists

Lists store multiple values.

skills = ["Python", "AI", "Data Analysis"]

Accessing list items:

print(skills[0])  # Python
print(skills[1])  # AI

Common list methods:

skills.append("Automation")
skills.insert(1, "Product Management")
skills.remove("AI")
skills.pop()
skills.sort()
skills.reverse()
4. Dictionaries

Dictionaries store key-value pairs.

profile = {
    "name": "Fares",
    "city": "Dubai",
    "target_role": "AI Product Manager",
    "skills": ["Python", "AI", "Data Analysis"]
}

Accessing dictionary values:

print(profile["name"])
print(profile["skills"][1])

Output:

Fares
AI

Useful dictionary methods:

profile.keys()
profile.values()
profile.items()

.items() returns key-value pairs, usually as tuples:

("name", "Fares")
("city", "Dubai")
5. Tuples

A tuple is an ordered group of values that cannot be changed.

person = ("Fares", "Dubai", "AI Product Manager")

Accessing tuple values:

print(person[0])
print(person[1])
6. Conditions

Conditions allow Python to make decisions.

score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")

Operators learned:

==: equal
!=: not equal
>: greater than
<: less than
>=: greater than or equal
<=: less than or equal
7. Loops

Loops repeat actions.

Loop through a list
skills = ["Python", "AI", "Data Analysis"]

for skill in skills:
    print("I am learning", skill)
Loop using range
for day in range(1, 6):
    print("Day", day, "- Learning Python")
Loop through a dictionary
profile = {
    "name": "Fares",
    "city": "Dubai",
    "target_role": "AI Product Manager"
}

for key, value in profile.items():
    print(key, ":", value)
While loop
count = 1

while count <= 5:
    print("Practice round", count)
    count = count + 1
8. Functions

Functions are reusable blocks of code.

def greet_user(name):
    print("Hello", name)

greet_user("Fares")

A function can return a value:

def calculate_progress(completed_days, total_days):
    progress = completed_days / total_days * 100
    return round(progress, 2)

progress = calculate_progress(2, 30)

print(progress)
Key Concept Notes
Function vs Method

A function is called directly:

len(skills)
print(skills)
type(skills)

A method belongs to an object:

skills.append("Automation")
profile.items()

Pattern:

function(object)
object.method()
Parameter vs Argument
def greet_user(name):
    print("Hello", name)

greet_user("Fares")
name is the parameter
"Fares" is the argument
print() vs return

print() displays information on the screen.

return sends a value back so it can be reused.

Day 2 Mini Project
# Day 2 Python Basics Notebook
# Fares Wali

TOTAL_DAYS = 30


def calculate_progress(completed_days, total_days):
    progress = completed_days / total_days * 100
    return round(progress, 2)


def check_role(role):
    role = role.strip().lower()

    if role == "ai product manager":
        return "Product + AI focus"
    elif role == "data analyst":
        return "Data focus"
    elif role == "consultant":
        return "Business transformation focus"
    else:
        return "Role not recognized"


name = "Fares"
city = "Dubai"
target_role = "AI Product Manager"
years_experience = 8
completed_days = 2
skills = ["Python", "AI", "Data Analysis", "Product Management"]

skills.append("Automation")

profile = {
    "name": name,
    "city": city,
    "target_role": target_role,
    "years_experience": years_experience,
    "skills": skills
}

progress = calculate_progress(completed_days, TOTAL_DAYS)
role_category = check_role(target_role)

print("Profile:")
for key, value in profile.items():
    print(key, ":", value)

print("\nProgress:", progress, "%")
print("Role category:", role_category)
Clean Code Rules Learned

Use this order:

Imports
Constants
Functions
Main variables
Main logic
Output

Important rules:

Define functions before using them
Use 4 spaces for indentation
Keep variables close to where they are used
Use uppercase for constants
Keep related logic together
Day 2 Completion Summary

Completed:

Variables
Data types
Lists
List methods
Dictionaries
Dictionary methods
Tuples
Conditions
Boolean logic basics
Loops
Functions
Parameters and arguments
print() vs return
Clean code structure and indentation

Next:

Day 3: Python for Data and pandas basics.
