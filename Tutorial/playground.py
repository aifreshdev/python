import math

# String
your_name = input("enter your name: ")
username = "I\'m " + your_name
print(username)

your_introduction = """
    I'm is a programmer.
"""
print(your_introduction)

your_job = 'Developer.'
print(your_job)
print(your_job[-2])
print(your_job[0:3])
print(your_job[1:])
print(your_job[:3])
print(your_job[1:-1])

last_name = "Li"
first_name = "Vincent"
full_name = f'{first_name} {last_name}'
print(full_name)

print("Python is great.".lower().find("thon"))
print("Python is great.".find("T"))

# Number
print(10 ** 3)
print(10 + 3 * 2 ** 2)
print(round(0.9))
print(abs(-2.9))
print(math.ceil(0.8))
print(math.floor(0.9))

# if else
is_hot = True
is_cold = False
is_liquid = True
is_soda = True

if is_hot:
    print("Water is hot.")
elif is_cold:
    print("Water is cold.")
else:
    print("Only water.")

if is_liquid and is_soda:
    print("Drink soda.")

if is_hot or is_cold:
    print("Is ok.")

if is_hot and not is_cold:
    print("This is cake.")

# for loop
for item in range(5, 10, 2):
    print(f"item {item}")

