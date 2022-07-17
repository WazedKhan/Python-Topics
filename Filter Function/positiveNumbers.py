import time

nums = [-2, -1, 0, 1, 2]

# return a new list containing only those numbers greater than 0.

# In regular for loop

regularStart = time.time()
def positive_numbers(nums):
    positive_nums = []
    for i in nums:
        if i > 0:
            positive_nums.append(i)

    return positive_nums
regularEnd = time.time()

# In filtering

filterStart = time.time()

filtered_nums = filter(lambda n: n > 0, nums)

filterEnd = time.time()


print(positive_numbers(nums), f'Execution time in regular loop: {regularEnd - regularStart}')
print(list(filtered_nums), f'Execution time in Filter function : {filterEnd - filterStart}')