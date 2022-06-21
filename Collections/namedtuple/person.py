from collections import namedtuple

Person = namedtuple('Person', 'name children')
john = Person("John Doe", ["Jimmy", "Timmy"])
print(john)

print(id(john.children))