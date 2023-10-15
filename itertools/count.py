"""
Itertools.count()
itertools.count() are generally used with map() to generate consecutive data points which is useful in
when working with data. It can also be used with zip to add sequences by passing count as parameter.
Parameters:
start: Start of the sequence (defaults to 0)
step: Difference between consecutive numbers (defaults to 1)

Returns: Returns a count object whose .__next__() method returns consecutive values.
"""


# Example #1: Creating evenly spaced list of numbers
# itertools.count() can be used to generate infinite recursive sequences easily. Lets have a look
import time
from icecream import ic
from itertools import count, islice

numbers = islice(count(10, 2), 10)

for index, num in enumerate(numbers):
    ic(index, num)

# create a count iterator object for evens
iterator = count(start=0, step=2)

evens = [next(iterator) for _ in range(5)]

# create a count iterator object odds
iterator = count(start=1, step=2)

odds = [next(iterator) for _ in range(5)]

ic(evens)
ic(odds)

"""
Example #2: Emulating enumerate() using itertools.count()
As mentioned earlier, count() can be used with zip().
Let’s see how can we use it to mimic the functionality of enumerate() without even knowing the length of list beforehand!
"""


# Program to emulate enumerate()
# using count()

# list containing some strings
my_list = ["Bruch", "Clerk", "Barry"]

# count spits out integers for
# each value in my list
for i in zip(count(start=1, step=1), my_list):
    ic(i)


# Assigning Unique Identifiers with count


class Object:
    """
    Represents an object with a unique ID.

    Args:
        name (str): The name of the object.

    Attributes:
        name (str): The name of the object.
        id (int): The unique ID of the object.

    Example:
        ```python
        obj = Objects("example")
        print(obj.name)  # Output: "example"
        print(obj.id)  # Output: <unique ID>
        ```"""

    _id_counter = count(1000)

    def __init__(self, name) -> None:
        self.name = name
        self.id = next(self._id_counter)


snowy = Object("Snowy")
spike = Object("Spike")

ic(snowy.name)
ic(snowy.id)

ic(spike.name)
ic(spike.id)


start = 0
step = 3

# Generating Timestamps or Time Intervals:
timestamp = count(time.time(), 1.0)
for _ in range(10):
    ic(next(timestamp))
    time.sleep(1)


for i in count():
    if i >= 100:
        break
    print(f"Progress: {i}%")
    time.sleep(0.1)
