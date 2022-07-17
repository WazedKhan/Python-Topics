# Extracting Even Numbers

numbers = [1, 3, 10, 45, 6, 50]

# Using filter function
evenNumbers = filter(lambda x: x % 2 == 0, numbers)
print(list(evenNumbers))
