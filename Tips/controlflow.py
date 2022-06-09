def print_one(x):
    print('One: ',x)

def print_two(x):
    print('Two: ',x)

def print_default(x):
    print('Default: ',x)

x = int(input())

# else-elif-else

"""
if x == 1:
    print_one(x)
elif x == 2:
    print_two(x)
else:
    print_default(x)
"""

# The condition can be relpaced by dict
actions = {1:print_one, 2:print_two}

action = actions.get(x, print_default)
action(x)