# Day 1 Python Practice
# Goal: Practise basic Python concepts

name = "Fares"
target_role = "AI Product Manager"
skills = ["Python", "SQL", "AI", "Product Management"]

print("Hello, my name is " + name)
print("My target role is " + target_role)
print("Skills I am learning:")

for skill in skills:
    print("- " + skill)


def introduce_person(name, role):
    return "My name is " + name + " and I am learning to become an " + role


message = introduce_person(name, target_role)
print(message)
