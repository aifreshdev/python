import math

print(bin(5))  # 0b101
print(bin(True))
print(int("0b101", 2))

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

name = ["Vincent", "Li"]

label = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9]]
pixel = [[11, 12, 13], [14, 15, 16], [17, 18, 19], [20, 21, 22]]
train_data = []
train_data.append([label, pixel])
print(train_data)

new_name = name[:]  # copy array
new_name[0] = "Jack"
print(new_name)

name.append("is Programmer")
print(name)

name.insert(2, "is man")
print(name)

name.extend(["is Programmer", "Good!"])
print(name)

name.pop()
name.pop()
name.pop(0)
print(name)

print("Li" in name)
print(name.count("Li"))

sentence = "!"
new_sentence = sentence.join(["ja", "ha", "oh"])
print(new_sentence)

print("Name %s %s" % (first_name, last_name))
print("Python is great.".lower().find("thon"))
print("Python is great.".find("T"))
print("Python is {}, I\' love {}".format("great", "it"))
print("Python is {1}, I\' love {0}".format("great", "it"))
print("Python is {k}, I\' love {e}".format(k="great", e="it"))

# Number
print(10 ** 3)
print(10 + 3 * 2 ** 2)
print(round(0.9))
print(abs(-2.9))
print(math.ceil(0.8))
print(math.floor(0.9))
print(2 ** 3)  # 8
print(5 // 10)  # 0
print(6 % 4)  # 2

a, b, c, *other, d = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(other)
print(d)

user = {
    'first_name': 'Vincent',
    'last_name': 'Li'
}

print(user.get('name', 'jack'))

user2 = dict(your_name="Vincent Li", address="example@gmail.com")
print(user2)
print(user2.pop('your_name'))
print(user2)
print(user2.update({'address': '123@abc.com'}))
print(user2)

print(user2.update({'email': 'example@mail.com'}))
print(user2)

user = {
    (1, 2): 'Vincent',
    'last_name': 'Li'
}

print(user[(1, 2)])

# tuple can't edit and remove
new_tuple = (1, 2, 3, 4, 5)

my_set = {1, 2, 3, 4, 5}
new_set = {1, 3, 7, 6, 8, 9}
print(new_set.difference(my_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(new_set))
print(my_set.intersection(new_set))
print(my_set.isdisjoint(new_set))  # check tow object is same content
print(my_set.union(new_set))  # merge and remove duplicate


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

# loop in step 2 (start, max, step)
for item in range(5, 10, 2):
    print(f"item {item}")

for item in range(10, 0, -1):
    print(f"item {item}")

for item in "hello world":
    print(item)

for i, char in enumerate("hello world"):
    print(i, char)

user = {
    'first_name': 'Vincent',
    'last_name': 'Li'
}

for item in user.items():
    key, value = item
    print(key, value)


for k, v in user.items():
    print(k, v)


for item in user.keys():
    print(item)

for item in user.values():
    print(item)

is_friend = True
can_message = "Hello My Friend!!" if is_friend else "hi gay!"
print(can_message)


a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)


def say_hello():
    print("hello")


say_hello()

# if the name of method is same that will be override
# Python allow only one name of method is same when it compiler


def say_hello(name, email="example@mail.com"):
    print(name, email)


def say_hello2(name="vincent li", email="example@mail.com"):
    print(name, email)


say_hello("jack")

# nested function


def sum1(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)


total = sum1(2, 4)
print(total)


def test(a):
    '''
    Info: test function major run to testing the comment.
    '''
    print(a)


help(test)

# magic function
print(test.__doc__)


def add_more(*args):
    print(args)
    return sum(args)


print(add_more(1, 2, 3, 4, 5))


def add_title(*args, **keys):
    print(keys)
    return sum(args)


print(add_title(1, 2, 3, 4, 5, num1=2, num2=3))


def add_name(name, *args, msg='hi', **keys):
    print(keys)
    return sum(args)


print(add_name('vincent', 1, 2, 3, 4, 5, num1=2, num2=3))


a = 1


def parent():
    a = 10
    return a


def parent2():
    return a


print(parent())
print(parent2())
print(a)


total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner : ", x)

    inner()
    print("outer: ", x)


outer()
