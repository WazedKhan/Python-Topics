# Variables without casting

number = 10 # number is int type
char = "String" # char is tring type
points = 5.21

# Declaring Variables with Casting

c_number = int(10)
c_char = str("String")
c_float = float(5.21)

print(f'Casting Int Var: {type(c_number)}, Without Casting Int Var: {type(number)}')
print(f'Casting Str Var: {type(c_char)}, Without Casting Str Var: {type(char)}')
print(f'Casting Float Var: {type(c_float)}, Without Casting Float Var: {type(points)}')

# object and reference
x = 300
y = 300

print(x)

x = y = z = 100
print(x, y, z)