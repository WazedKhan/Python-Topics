# Finding Prime Numbers

import time
import math

startTime = time.perf_counter()
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

primeNumbers = list(filter(is_prime, range(1, 51)))
endTime = time.perf_counter()

print(primeNumbers)
print(f'Time: {endTime - startTime}')