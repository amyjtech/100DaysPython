# Map
# Looping without a loop


# Basic usage - count len
people = ['Matt', 'Bryan', 'Nicole', 'Tammy']


# OLD way
'''count = []
for x in people:
    count.append(len(x))
print(f'Old way:\n{count}')'''

# MODERN way
print(f'Map function:\n{list(map(len,people))}')


# COMBINE ELEMENTS
# Notice different lengs, we are also passing multiple args

base = ('Pie', 'Cake', 'Brownies')
toppings = ('Apple', 'Chocolate', 'Fudge', 'Pizza')


def merg(a, b):
    return a + ' ' + b


x = map(merg, base, toppings)
print(list(x))
# If there is nothing matched up it will fall off -> pizza toppings


# MULTIPE FUNCTIONS
# call multiple functions in one map call

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def doall(func, num):
    return func(num[0], num[1])


# Tuple with all the functions
f = (add, subtract, multiply, divide)

# list inside a list
v = [[5, 3]]
n = list(v) * len(f)
print(f'{n}\n')
m = map(doall, f, n)
print(list(m))
