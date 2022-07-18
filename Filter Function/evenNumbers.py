# Extracting Even Numbers

numbers = [1, 3, 10, 45, 6, 50]

sqrEven =  list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

print(sqrEven)