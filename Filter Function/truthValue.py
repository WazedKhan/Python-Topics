# list contains only those values that are truthy in Python

# objects = [0, 1, [], 4, 5, "", None, 8]
objects = [True, False, True]

def indentify(value):
    return value

print(list(filter(indentify, objects)))

"""
Note: Python follows a set of rules to determine an object’s truth value.

For example, the following objects are falsy:

1. Constants like None and False
2. Numeric types with a zero value, like 0, 0.0, 0j, Decimal(0), and Fraction(0, 1)
3. Empty sequences and collections, like "", (), [], {}, set(), and range(0)
4. Objects that implement __bool__() with a return value of False or __len__() with a return value of 0

Any other object will be considered truthy.

"""

print(list(filter(None, objects)))

# filter() tests every item in the input iterable using the Python rules you saw before.
# Then it yields those items that evaluate to True.

